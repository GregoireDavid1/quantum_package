BEGIN_SHELL [ /usr/bin/env python ]
from perturbation import perturbations
import os

filename = os.environ["QPACKAGE_ROOT"]+"/src/Perturbation/perturbation_template.f"
file = open(filename,'r')
template = file.read()
file.close()

for p in perturbations:
  print template.replace("$PERT",p)

END_SHELL
