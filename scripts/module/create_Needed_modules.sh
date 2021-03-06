#!/bin/bash
#
# Creates the initial NEEDED_MODULES file.
# This script is supposed to run in a module directory.
# Thu Apr  3 13:38:38 CEST 2014

if [[ -z ${QPACKAGE_ROOT} ]]
then
  print "The QPACKAGE_ROOT environment variable is not set."
  print "Please reload the quantum_package.rc file."
  exit -1
fi
source ${QPACKAGE_ROOT}/scripts/qp_include.sh

check_current_dir_is_module

OUTPUT=$(module_handler.py check_dependencies $@)

if [[ $? -eq 0 ]]
then
  echo $@ > NEEDED_CHILDREN_MODULES
fi