#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from utils.file_handles import read_log
from utils.esp import dump_esp
from utils.esp import dump_esp_gen

SMALL_SETS = ['H2O','ClH','NH3','CH4','CH2O','C2H2','C2H4','CH3Cl','CH3OH','oh2oh2','NH4+','CH3F']
LARGE_SETS = ['C2H6','C3H4','C3H8','C3N2H4','C3NOH3','C3NOH3p','C4H10',\
		'C4NH4','C4OH4','C5NH5','C6H6','CH3Br','CH3COCH3','CH3NH2','CH3OCH3',\
		'CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','NMA','PO3CH5']

# mapping the abbreviation to the full-length name
nl = {'321g':'3-21G','321pg':'3-21+G','631g':'6-31G*',\
		'631gss':'6-31++g**','6311g':'6-311++G**',\
		'2z':'cc-pvdz','a2z':'aug-cc-pvdz','3z':'cc-pvtz',\
		'a3z':'aug-cc-pvtz','4z':'cc-pvqz','a4z':'aug-cc-pvqz',\
		'5z':'cc-pv5z','a5z':'aug-cc-pv5z'}

nl = {'def2tzvppd': 'gen'}


#methods = ['hf','b3lyp','m06','m062x','mn15','wb97xd','ccsd','mp2']
#methods = ['ccsd','wb97xd']
#methods = ['wb97xd']
methods= ['ccsd']



#for small in SMALL_SETS:
#	for method in methods:
#		for k_bs, v_bs in nl.items():
#			log_file = 'OPT/SMALL/{}.log'.format(small)
#			esp_file = 'ESP/SMALL/{1}/{0}_{1}_{2}.gjf'.format(small,method,k_bs)
#
#			xyz = read_log(log_file)
#
#			if small == 'NH4+':
#				dump_esp(esp_file, small, xyz, k_bs, v_bs, method, charge=1, spin=1)
#			else:
#				dump_esp(esp_file, small, xyz, k_bs, v_bs, method, charge=0, spin=1)

#for large in LARGE_SETS:
#	for method in methods:
#		for k_bs, v_bs in nl.items():
#			log_file = 'OPT/LARGE/{}.log'.format(large)
#			esp_file = 'ESP/LARGE/{1}/{0}_{1}_{2}.gjf'.format(large,method,k_bs)
#
#			xyz = read_log(log_file)
#
#			dump_esp(esp_file, large, xyz, k_bs, v_bs, method, charge=0, spin=1)


for small in SMALL_SETS:
	for method in methods:
		for k_bs, v_bs in nl.items():
			log_file = 'OPT/SMALL/{}.log'.format(small)
			esp_file = 'ESP/SMALL/{2}/{0}_{1}_{2}.gjf'.format(small,method,k_bs)

			xyz = read_log(log_file)

			if small == 'NH4+':
				dump_esp_gen(esp_file, small, xyz, k_bs, v_bs, method, charge=1, spin=1)
			else:
				dump_esp_gen(esp_file, small, xyz, k_bs, v_bs, method, charge=0, spin=1)
