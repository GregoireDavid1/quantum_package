#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Welcom the ei_handler.
We will create all the ezfio related stuff from a EZFIO.cfg file.

Usage:
    ei_handler.py [--path] [--irpf90] [--ezfio_config] [--ocaml] [--ezfio_default] [--global]

By default all the option are executed.

Options:
    -h --help
    --path             The path of the `EZFIO.cfg`, by default will look in the ${pwd}
    --irpf90           Create the `ezfio_interface.irpf90`
                             which contains all the providers needed
                             (aka all with the `interface: input` parameter)
                             in `${pwd}`
    --ezfio_config     Create the `${module_lower}_ezfio_interface_config` in
                             `${QPACKAGE_ROOT}/EZFIO/config/`
                       This file is needed by *EZFIO* to create the `libezfio.so`
    --ocaml            Create the `Input_module.lower.ml` for the *qp_edit*
    --ezfio_default    Create the `${module_lower}_ezfio_interface_default` in
                             `${QPACKAGE_ROOT}/data/ezfio_defaults` needed by
                             the ocaml
    --global           Create all the stuff who need all the EZFIO.cfg

Format specification :
    [provider_name]  | the name of the provider in irp.f90
    doc:{str}        | Is the doc
    Type:{str}       | Is a fancy_type supported by the ocaml
    ezfio_name:{str} | Will be the name of the file for the ezfio
                       (optional by default is the name of the provider)
    interface:{str}  | The provider is a imput or a output
    default:{str}    | The default value if interface == input:
    size:{str}       | the size information
                        (like 1 or =sum(ao_num) or (ao_num,3) )

Example of EZFIO.cfg:
```
[thresh_SCF]
doc: Threshold on the convergence of the Hartree Fock energy
type: Threshold
default: 1.e-10
interface: input
size: 1

[energy]
type: double precision
doc: Calculated HF energy
interface: output
```
"""
from docopt import docopt

import sys
import os
import os.path

import ConfigParser

from collections import defaultdict
from collections import namedtuple


from qp_utils import cache

Type = namedtuple('Type', 'fancy ocaml fortran')


def is_bool(str_):
    """
    Take a string, if is a bool return the conversion into
        fortran and ocaml.
    """
    if "true" in str_.strip().lower():
        return Type(None, "true", ".True.")
    elif "false" in str_.strip().lower():
        return Type(None, "false", ".False")
    else:
        raise TypeError


@cache
def get_type_dict():
    """
    This function makes the correspondance between the type of value read in
    ezfio.cfg into the f90 and Ocaml Type
    return fancy_type[fancy_type] = namedtuple('Type', 'ocaml fortran')
    For example fancy_type['Ndet'].fortran = interger
                                  .ocaml   = int
    """
    # ~#~#~#~#~ #
    # P i c l e #
    # ~#~#~#~#~ #
    qpackage_root = os.environ['QPACKAGE_ROOT']

    # ~#~#~#~ #
    # I n i t #
    # ~#~#~#~ #

    fancy_type = defaultdict(dict)

    # ~#~#~#~#~#~#~#~ #
    # R a w _ t y p e #
    # ~#~#~#~#~#~#~#~ #

    fancy_type['integer'] = Type(None, "int", "integer")
    fancy_type['integer*8'] = Type(None, "int", "integer*8")

    fancy_type['int'] = Type(None, "int", "integer")

    fancy_type['float'] = Type(None, "float", "double precision")
    fancy_type['double precision'] = Type(None, "float", "double precision")

    fancy_type['logical'] = Type(None, "bool", "logical")
    fancy_type['bool'] = Type(None, "bool", "logical")

    fancy_type['character*(32)'] = Type(None, "string", "character*(32)")
    fancy_type['character*(64)'] = Type(None, "string", "character*(68)")
    fancy_type['character*(256)'] = Type(None, "string", "character*(256)")

    # ~#~#~#~#~#~#~#~ #
    # q p _ t y p e s #
    # ~#~#~#~#~#~#~#~ #

    # Dict to change ocaml LowLevel type into FortranLowLevel type
    ocaml_to_fortran = {"int": "integer",
                        "float": "double precision",
                        "logical": "logical",
                        "string": "character*32"}

    # Read and parse qptype generate
    src = qpackage_root + "/ocaml/qptypes_generator.ml"
    with open(src, "r") as f:
        r = f.read()

        # Generate
        l_gen = [i for i in r.splitlines() if i.strip().startswith("*")]

        # Untouch
        b = r.find('let untouched = "')
        e = r.find(';;', b)

        l_un = [i for i in r[b:e].splitlines() if i.strip().startswith("module")]

    # ~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~ #
    # q p _ t y p e s _ g e n e r a t e #
    # ~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~ #

    # Read the fancy_type, the ocaml. and convert the ocaml to the fortran
    for i in l_gen + l_un:
        str_fancy_type = i.split()[1].strip()
        str_ocaml_type = i.split()[3]

        if str_ocaml_type != 'sig':
            str_fortran_type = ocaml_to_fortran[str_ocaml_type]
        else:
            str_fortran_type = 'character*(32)'
            str_ocaml_type = 'string'

        fancy_type[str_fancy_type] = Type(str_fancy_type,
                                          str_ocaml_type,
                                          str_fortran_type)

    # ~#~#~#~#~#~#~#~ #
    # F i n a l i z e #
    # ~#~#~#~#~#~#~#~ #
    return dict(fancy_type)


type_dict = get_type_dict()


def get_dict_config_file(config_file_path, module_lower):
    """
    Input:
        config_file_path is the config file path
            (for example FULL_PATH/EZFIO.cfg)
        module_lower is the MODULE name lowered
            (Ex fullci)

    Return a dict d[provider_name] = {type,
                                      doc,
                                      ezfio_name,
                                      ezfio_dir,
                                      size,
                                      interface,
                                      default}

    - Type       : Is a Type named tuple who containt
                    fortran and ocaml type
    - doc        : Is the doc
    - ezfio_name : Will be the name of the file
    - ezfio_dir  : Will be the folder who containt the ezfio_name
        * /ezfio_dir/ezfio_name
        * equal to MODULE_lower name by default.
    - interface  : The provider is a imput or a output
    - default : The default value /!\ stored in a Type named type!
                   if interface == input
    - size : Is the string read in ezfio.cgf who containt the size information
         (like 1 or =sum(ao_num))
    """
    # ~#~#~#~ #
    # I n i t #
    # ~#~#~#~ #

    d = defaultdict(dict)
    l_info_required = ["doc", "interface"]
    l_info_optional = ["ezfio_dir", "ezfio_name", "size"]

    # ~#~#~#~#~#~#~#~#~#~#~ #
    # L o a d _ C o n f i g #
    # ~#~#~#~#~#~#~#~#~#~#~ #

    config_file = ConfigParser.ConfigParser()
    config_file.readfp(open(config_file_path))

    # ~#~#~#~#~#~#~#~#~ #
    # F i l l _ d i c t #
    # ~#~#~#~#~#~#~#~#~ #

    def error(o, p, c):
        "o option ; p provider_name ;c config_file_path"
        print "You need a {0} for {1} in {2}".format(o, p, c)

    for section in config_file.sections():
        # pvd = provider
        pvd = section.lower()

        # Create the dictionary who containt the value per default
        d_default = {"ezfio_name": pvd,
                     "ezfio_dir": module_lower,
                     "size": "1"}

        # Check if type if avalaible
        type_ = config_file.get(section, "type")
        if type_ not in type_dict:
            print "{0} not avalaible. Choose in:".format(type_)
            print ", ".join(sorted([i for i in type_dict]))
            sys.exit(1)
        else:
            d[pvd]["type"] = type_dict[type_]

        # Fill the dict with REQUIRED information
        for option in l_info_required:
            try:
                d[pvd][option] = config_file.get(section, option)
            except ConfigParser.NoOptionError:
                error(option, pvd, config_file_path)
                sys.exit(1)

        # Fill the dict with OPTIONAL information
        for option in l_info_optional:
            try:
                d[pvd][option] = config_file.get(section, option).lower()
            except ConfigParser.NoOptionError:
                if option in d_default:
                    d[pvd][option] = d_default[option]

        # If interface is input we need a default value information
        if d[pvd]["interface"].lower() == "input":
            try:
                default_raw = config_file.get(section, "default")
            except ConfigParser.NoOptionError:
                error("default", pvd, config_file_path)
                sys.exit(1)

            try:
                d[pvd]["default"] = is_bool(default_raw)
            except TypeError:
                d[pvd]["default"] = Type(None, default_raw, default_raw)

    return dict(d)


def create_ezfio_provider(dict_ezfio_cfg):
    import re

    """
    From dict d[provider_name] = {type,
                                  doc,
                                  ezfio_name,
                                  ezfio_dir,
                                  interface,
                                  default
                                  size}
    create the a list who containt all the code for the provider
    output = output_dict_info['ezfio_dir'
    return [code, ...]
    """

    from ezfio_generate_provider import EZFIO_Provider
    dict_code_provider = dict()

    ez_p = EZFIO_Provider()
    for provider_name, dict_info in dict_ezfio_cfg.iteritems():
        if "input" in dict_info["interface"]:
            ez_p.set_type(dict_info['type'].fortran)
            ez_p.set_name(provider_name)
            ez_p.set_doc(dict_info['doc'])
            ez_p.set_ezfio_dir(dict_info['ezfio_dir'])
            ez_p.set_ezfio_name(dict_info['ezfio_name'])
            ez_p.set_output("output_%s" % dict_info['ezfio_dir'])

            # (nuclei.nucl_num,pseudo.klocmax) => (nucl_num,klocmax)
            ez_p.set_size(re.sub(r'\w+\.', "", dict_info['size']))

            dict_code_provider[provider_name] = str(ez_p) + "\n"

    return dict_code_provider


def save_ezfio_provider(path_head, dict_code_provider):
    """
    Write in path_head/"ezfio_interface.irp.f" the value of dict_code_provider
    """

    path = "{0}/ezfio_interface.irp.f".format(path_head)

    try:
        f = open(path, "r")
    except IOError:
        old_output = ""
    else:
        old_output = f.read()
        f.close()

    l_output = ["! DO NOT MODIFY BY HAND",
                "! Created by $QPACKAGE_ROOT/scripts/ezfio_interface.py",
                "! from file {0}/EZFIO.cfg".format(path_head),
                "\n"]

    l_output += [code for code in dict_code_provider.values()]

    output = "\n".join(l_output)

    if output != old_output:
        with open(path, "w+") as f:
            f.write(output)


def create_ezfio_stuff(dict_ezfio_cfg, config_or_default="config"):
    """
    From dict_ezfio_cfg[provider_name] = {type, default, ezfio_name,ezfio_dir,doc}
    Return the string ezfio_interface_config
    """

    def size_format_to_ezfio(size_raw):
        """
        If size_raw == "=" is a formula -> do nothing; return
        Else convert the born of a multidimential array
           (12,begin:end) into (12,begin+end+1) for example
        If the value are between parenthses ->  do nothing; return
        """

        size_raw = str(size_raw)
        if size_raw.startswith('='):
            size_convert = size_raw
        else:
            size_raw = provider_info["size"].translate(None, "()")
            size_raw = size_raw.replace('.', '_')

            a_size_raw = []
            for dim in size_raw.split(","):
                try:
                    (begin, end) = map(str.strip, dim.split(":"))
                except ValueError:
                    a_size_raw.append(dim)
                else:
                    if begin[0] == '-':
                        a_size_raw.append("{0}+{1}+1".format(end, begin[1:]))
                    else:
                       a_size_raw.append("{0}-{1}+1".format(end, begin))

            size_raw = ",".join(a_size_raw)

            size_convert = "({0})".format(size_raw)
        return size_convert

    def create_format_string(size):
        """
        Take a size number and
            return the string format for being right align with this offset
        """
        return "{{0:<{0}}}".format(size).format

    # ~#~#~#~#~#~#~#~#~#~#~# #
    #  F o r m a t _ i n f o #
    # ~#~#~#~#~#~#~#~#~#~#~# #

    lenmax_name = max([len(i) for i in dict_ezfio_cfg])
    lenmax_type = max([len(i["type"].fortran)
                       for i in dict_ezfio_cfg.values()])

    str_name_format = create_format_string(lenmax_name + 2)
    str_type_format = create_format_string(lenmax_type + 2)

    # ~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~# #
    #  C r e a t e _ t h e _ s t r i n g #
    # ~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~# #

    # Checking is many ezfio_dir provided
    l_ezfio_dir = [d['ezfio_dir'] for d in dict_ezfio_cfg.values()]

    if not l_ezfio_dir.count(l_ezfio_dir[0]) == len(l_ezfio_dir):
        print >> sys.stderr, "You have many ezfio_dir. Not supported yet"
        raise TypeError
    else:
        result = [l_ezfio_dir[0]]

    for provider_name, provider_info in sorted(dict_ezfio_cfg.iteritems()):

        # Get the value from dict
        name_raw = provider_info["ezfio_name"].lower()

        fortran_type_raw = provider_info["type"].fortran

        if "size" in provider_info and not provider_info["size"] == "1":
            size_raw = provider_info["size"]
        else:
            size_raw = None

        # It is the last so we don't need to right align it
        str_size = size_format_to_ezfio(size_raw) if size_raw else ""

        # Get the string in to good format (left align and co)
        str_name = str_name_format(name_raw)
        str_fortran_type = str_type_format(fortran_type_raw)

        # Return the string
        if config_or_default == "config":
            s = "  {0} {1} {2}".format(str_name, str_fortran_type, str_size)
        elif config_or_default == "default":
            try:
                str_value = provider_info["default"].ocaml
            except KeyError:
                continue
            else:
                s = "  {0} {1}".format(str_name, str_value)
        else:
            raise KeyError
        # Append
        result.append(s)

    return "\n".join(result)


def create_ezfio_config(dict_ezfio_cfg):
    return create_ezfio_stuff(dict_ezfio_cfg,
                              config_or_default="config")


def save_ezfio_config(module_lower, str_ezfio_config):
    """
    Write the str_ezfio_config in
    "$QPACKAGE_ROOT/EZFIO/{0}.ezfio_interface_config".format(module_lower)
    """

    root_ezfio = "{0}/EZFIO".format(os.environ['QPACKAGE_ROOT'])
    path = "{0}/config/{1}.ezfio_interface_config".format(root_ezfio,
                                                          module_lower)

    try:
        f = open(path, "r")
    except IOError:
        old_output = ""
    else:
        old_output = f.read()
        f.close()

    if str_ezfio_config != old_output:
        with open(path, "w+") as f:
            f.write(str_ezfio_config)


def create_ezfio_default(dict_ezfio_cfg):
    return create_ezfio_stuff(dict_ezfio_cfg,
                              config_or_default="default")


def save_ezfio_default(module_lower, str_ezfio_default):
    """
    Write the str_ezfio_config in
    "$QPACKAGE_ROOT/data/ezfio_defaults/{0}.ezfio_interface_default".format(module_lower)
    """

    root_ezfio_default = "{0}/data/ezfio_defaults/".format(
        os.environ['QPACKAGE_ROOT'])
    path = "{0}/{1}.ezfio_interface_default".format(root_ezfio_default,
                                                    module_lower)

    try:
        f = open(path, "r")
    except IOError:
        old_output = ""
    else:
        old_output = f.read()
        f.close()

    if str_ezfio_default != old_output:
        with open(path, "w+") as f:
            f.write(str_ezfio_default)


def create_ocaml_input(dict_ezfio_cfg, module_lower):

    # ~#~#~#~# #
    #  I n i t #
    # ~#~#~#~# #

    from ezfio_generate_ocaml import EZFIO_ocaml

    l_ezfio_name = []
    l_type = []
    l_doc = []

    for k, v in dict_ezfio_cfg.iteritems():
        if v['interface'] == "input":
            l_ezfio_name.append(v['ezfio_name'])
            l_type.append(v["type"])
            l_doc.append(v["doc"])

    if not l_ezfio_name:
        raise ValueError

    e_glob = EZFIO_ocaml(l_ezfio_name=l_ezfio_name,
                         l_type=l_type,
                         l_doc=l_doc)

    # ~#~#~#~#~#~#~#~# #
    #  C r e a t i o n #
    # ~#~#~#~#~#~#~#~# #

    template = ['(* =~=~ *)',
                '(* Init *)',
                '(* =~=~ *)',
                ""]

    template += ["open Qptypes;;",
                 "open Qputils;;",
                 "open Core.Std;;",
                 "",
                 "module {0} : sig".format(module_lower.capitalize())]

    template += [e_glob.create_type()]

    template += ["  val read  : unit -> t option",
                 "  val write : t-> unit",
                 "  val to_string : t -> string",
                 "  val to_rst : t -> Rst_string.t",
                 "  val of_rst : Rst_string.t -> t option",
                 "end = struct"]

    template += [e_glob.create_type()]

    template += ['',
                 '  let get_default = Qpackage.get_ezfio_default "{0}";;'.format(module_lower),
                 '']

    template += ['(* =~=~=~=~=~=~==~=~=~=~=~=~ *)',
                 '(* Generate Special Function *)',
                 '(* =~=~=~==~=~~=~=~=~=~=~=~=~ *)',
                 ""]

    for provider_name, d_val in sorted(dict_ezfio_cfg.iteritems()):

        if 'default' not in d_val:
            continue

        ezfio_dir = d_val["ezfio_dir"]
        ezfio_name = d_val["ezfio_name"]

        e = EZFIO_ocaml(ezfio_dir=ezfio_dir,
                        ezfio_name=ezfio_name,
                        type=d_val["type"])

        template += [e.create_read(),
                     e.create_write(),
                     ""]

    template += ['(* =~=~=~=~=~=~=~=~=~=~=~=~ *)',
                 '(* Generate Global Function *)',
                 '(* =~=~=~=~=~=~=~=~=~=~=~=~ *)',
                 ""]

    template += [e_glob.create_read_global(),
                 e_glob.create_write_global(),
                 e_glob.create_to_string(),
                 e_glob.create_to_rst()]

    template += ["  include Generic_input_of_rst;;",
                 "  let of_rst = of_rst t_of_sexp;;",
                 "",
                 "end"]

    return "\n".join(template)


def save_ocaml_input(module_lower, str_ocaml_input):
    """
    Write the str_ocaml_input in
    $QPACKAGE_ROOT/ocaml/Input_{0}.ml".format(module_lower)
    """

    path = "{0}/ocaml/Input_{1}.ml".format(os.environ['QPACKAGE_ROOT'],
                                           module_lower)

    try:
        f = open(path, "r")
    except IOError:
        old_output = ""
    else:
        old_output = f.read()
        f.close()

    if str_ocaml_input != old_output:
        with open(path, "w+") as f:
            f.write(str_ocaml_input)


def get_l_module_lower():
    """
    Get all module who have EZFIO.cfg with input data
        (NB `search` in all the ligne and `match` only in one)
    """

    # ~#~#~#~ #
    # I n i t #
    # ~#~#~#~ #

    mypath = "{0}/src".format(os.environ['QPACKAGE_ROOT'])

    # ~#~#~#~#~#~#~#~ #
    # L _ f o l d e r #
    # ~#~#~#~#~#~#~#~ #

    from os import listdir
    from os.path import isdir, join, exists

    l_folder = [f for f in listdir(mypath) if isdir(join(mypath, f))]

    # ~#~#~#~#~#~#~#~#~#~#~#~#~#~ #
    # L _ m o d u l e _ l o w e r #
    # ~#~#~#~#~#~#~#~#~#~#~#~#~#~ #

    l_module_lower = []
    import re
    p = re.compile(ur'interface:\s+input')

    for f in l_folder:
        path = "{0}/{1}/EZFIO.cfg".format(mypath, f)
        if exists(path):
            with open(path, 'r') as file_:
                if p.search(file_.read()):
                    l_module_lower.append(f.lower())

    # ~#~#~#~#~#~ #
    # R e t u r n #
    # ~#~#~#~#~#~ #

    return l_module_lower


def create_ocaml_input_global():
    """
    Check for all the EZFIO.cfg get the module lower
    then create incule {module_lower}.ml
    """

    # ~#~#~#~# #
    #  I n i t #
    # ~#~#~#~# #

    l_module_lower = get_l_module_lower()

    # ~#~#~#~#~#~#~#~# #
    #  C r e a t i o n #
    # ~#~#~#~#~#~#~#~# #

    from ezfio_generate_ocaml import EZFIO_ocaml

    qpackage_root = os.environ['QPACKAGE_ROOT']
    path = qpackage_root + "/scripts/ezfio_interface/qp_edit_template"

    with open(path, "r") as f:
        template_raw = f.read()

    e = EZFIO_ocaml(l_module_lower=l_module_lower)

    template = template_raw.format(keywords=e.create_qp_keywords(),
                                   keywords_to_string=e.create_qp_keywords_to_string(),
                                   section_to_rst=e.create_qp_section_to_rst(),
                                   write=e.create_qp_write(),
                                   tasks=e.create_qp_tasks())

    input_auto = e.create_input_auto_generated()

    return (template, input_auto)


def save_ocaml_input_auto(str_ocaml_input_global):
    """
    Write the str_ocaml_input in
    $QPACKAGE_ROOT/ocaml/Input_auto_generated.ml
    """

    path = "{0}/ocaml/Input_auto_generated.ml".format(os.environ['QPACKAGE_ROOT'])

    try:
        f = open(path, "r")
    except IOError:
        old_output = ""
    else:
        old_output = f.read()
        f.close()

    if str_ocaml_input_global != old_output:
        with open(path, "w+") as f:
            f.write(str_ocaml_input_global)


def save_ocaml_qp_edit(str_ocaml_qp_edit):
    """
    Write the str_ocaml_qp_edit in
    $QPACKAGE_ROOT/ocaml/qp_edit.ml
    """

    path = "{0}/ocaml/qp_edit.ml".format(os.environ['QPACKAGE_ROOT'])

    try:
        f = open(path, "r")
    except IOError:
        old_output = ""
    else:
        old_output = f.read()
        f.close()

    if str_ocaml_qp_edit != old_output:
        with open(path, "w+") as f:
            f.write(str_ocaml_qp_edit)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    # ___
    #  |  ._  o _|_
    # _|_ | | |  |_
    #

    if not arguments["--global"]:
        if not arguments["--path"]:
            config_file_path = "EZFIO.cfg"
            if "EZFIO.cfg" not in os.listdir(os.getcwd()):
                sys.exit(0)
        else:
            config_file_path = arguments["path"]

        # Get the full path
        config_file_path = os.path.expanduser(config_file_path)
        config_file_path = os.path.expandvars(config_file_path)
        config_file_path = os.path.abspath(config_file_path)

        # ~#~#~#~#~#~#~#~#~#~#~#~#~#~# #
        #  G e t _ m o d u l e _ d i r #
        # ~#~#~#~#~#~#~#~#~#~#~#~#~#~# #

        path_dirname = os.path.dirname(config_file_path)
        module = [i for i in path_dirname.split("/") if i][-1]
        module_lower = module.lower()

        # Because we only authorise this right now!
        ezfio_dir = module_lower
        dict_ezfio_cfg = get_dict_config_file(config_file_path, ezfio_dir)

    #  _
    # /   _   _|  _     _   _  ._   _  ._ _. _|_ o  _  ._
    # \_ (_) (_| (/_   (_| (/_ | | (/_ | (_|  |_ | (_) | |
    #                   _|

    # ~#~#~#~#~#~#~#~#~#~ #
    # W h a t _ t o _ d o #
    # ~#~#~#~#~#~#~#~#~#~ #
    if any([arguments[i] for i in ["--irpf90",
                                   "--ezfio_config",
                                   "--ocaml",
                                   "--ezfio_default",
                                   "--global"]]):
        # User changer somme argument, do what he want
        do_all = False
    else:
        # Do all the stuff
        do_all = True

    # ~#~#~#~#~#~#~ #
    # I R P . f 9 0 #
    # ~#~#~#~#~#~#~ #

    if do_all or arguments["--irpf90"]:
        l_str_code = create_ezfio_provider(dict_ezfio_cfg)
        save_ezfio_provider(path_dirname, l_str_code)

    # ~#~#~#~#~#~#~#~#~#~#~#~ #
    # e z f i o _ c o n f i g #
    # ~#~#~#~#~#~#~#~#~#~#~#~ #

    if do_all or arguments["--ezfio_config"]:
        str_ezfio_config = create_ezfio_config(dict_ezfio_cfg)
        save_ezfio_config(module_lower, str_ezfio_config)

    # ~#~#~#~#~#~#
    # O c a m l #
    # ~#~#~#~#~#~#
    if do_all or arguments["--ocaml"]:
        try:
            str_ocaml_input = create_ocaml_input(dict_ezfio_cfg, module_lower)
        except ValueError:
            pass
        else:
            save_ocaml_input(module_lower, str_ocaml_input)

    # ~#~#~#~#~#~#~#~#~#~#~#~#~ #
    # e z f i o _ d e f a u l t #
    # ~#~#~#~#~#~#~#~#~#~#~#~#~ #
    if do_all or arguments["--ezfio_default"]:
        str_ezfio_default = create_ezfio_default(dict_ezfio_cfg)
        save_ezfio_default(module_lower, str_ezfio_default)

    # ~#~#~#~#~#~#~#~#~#~#~#~#~ #
    # e z f i o _ d e f a u l t #
    # ~#~#~#~#~#~#~#~#~#~#~#~#~ #

    if do_all or arguments["--global"]:
        str_ocaml_qp_edit, str_ocaml_input_auto = create_ocaml_input_global()
        save_ocaml_input_auto(str_ocaml_input_auto)
        save_ocaml_qp_edit(str_ocaml_qp_edit)
