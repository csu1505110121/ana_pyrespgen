#!/bi/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from utils.file_handles import read_pdb
from utils.opt import dump_opt

SMALL_SETS = ['H2O','ClH','NH3','CH4','CH2O','C2H2','C2H4','CH3Cl','CH3OH','oh2oh2','NH4+','CH3F']
LARGE_SETS = ['C2H6','C3H4','C3H8','C3N2H4','C3NOH3','C3NOH3p','C4H10',\
				'C4NH4','C4OH4','C5NH5','C6H6','CH3Br','CH3COCH3','CH3NH2','CH3OCH3',\
				'CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','NMA','PO3CH5']

# Here is for SMALL SETS

for small in SMALL_SETS:
	pdb_file = 'XYZ/SMALL/{}.pdb'.format(small)
	opt_file = 'OPT/SMALL/{}.gjf'.format(small)
	xyz = read_pdb(pdb_file)
	#print(xyz)
	if small == 'NH4+':
		dump_opt(opt_file,small,xyz,charge=1,spin=1)
	else:
		dump_opt(opt_file,small,xyz,charge=0,spin=1)

# Here is for LARGE SETS
for large in LARGE_SETS:
	pdb_file = 'XYZ/LARGE/{}.pdb'.format(large)
	opt_file = 'OPT/LARGE/{}.gjf'.format(large)
	xyz = read_pdb(pdb_file)
	
	dump_opt(opt_file,large,xyz,charge=0,spin=1)
