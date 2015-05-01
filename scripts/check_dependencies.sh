#!/bin/bash
# 
# usage:
#  check_dependencies.sh MOs AOs Electrons
#
# Checks that the list of dependencies given in
# argument is consistent. If the dependencies
# are OK the exit code is 0, otherwise it is 1. 
# If no argument is given, the dependencies are
# read in the Makefile.
# Thu Apr  3 01:44:23 CEST 2014

if [[ -z ${QPACKAGE_ROOT} ]]
then
  print "The QPACKAGE_ROOT environment variable is not set."
  print "Please reload the quantum_package.rc file."
  exit -1
fi
source ${QPACKAGE_ROOT}/scripts/qp_include.sh

if [[ -z $1 ]]
then
  exit 0
fi

if [[ $1 == "-" ]]
then
  COMMAND_LINE=$(only_children_to_all_genealogy.py NEEDED_MODULES)
else
  COMMAND_LINE=$(unique_list $@)
fi

for d in $COMMAND_LINE
do
  if [[ ! -d ${QPACKAGE_ROOT}/src/$d ]]
  then
    echo Error: Directory $d does not exist 
    exit 2
  fi

done

DEPS_LONG=""
for i in $COMMAND_LINE
do
  DEPS_LONG+=" $i "
  DEPS_LONG+=$(only_children_to_all_genealogy.py "${QPACKAGE_ROOT}/src/${i}/NEEDED_MODULES")
done

DEPS=$(unique_list $DEPS_LONG)

if [[ ! "$COMMAND_LINE" == "$DEPS" ]]
then
  DEPS=$(${QPACKAGE_ROOT}/scripts/check_dependencies.sh ${DEPS})
fi
echo "$DEPS"

if [[ "$COMMAND_LINE" == "$DEPS" ]]
then
  exit 0
else
  exit 1
fi
