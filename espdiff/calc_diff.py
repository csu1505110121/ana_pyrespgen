#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import glob
from espdiff.esputils import ESP_rmsd
import os

output1 = open('ESP_RMSD_diff.txt','w')
output2 = open('ESP_RRMSD_diff.txt','w')

# mapping the abbreviation to the full-length name
nl = {'321g':'3-21G','321pg':'3-21+G','631g':'6-31G*',\
		'631gss':'6-31++g**','6311g':'6311++G**',\
		'2z':'cc-pvdz','a2z':'aug-cc-pvdz','3z':'cc-pvtz',\
		'a3z':'aug-cc-pvtz','4z':'cc-pvqz','a4z':'aug-cc-pvqz',\
		'5z':'cc-pv5z','a5z':'aug-cc-pv5z'}

mols = ['C2H6','C3H4','C3H8','C3N2H4','C3NOH3','C3NOH3p','C4H10',\
		'C4NH4','C4OH4','C5NH5','C6H6','CH3Br','CH3COCH3','CH3NH2','CH3OCH3',\
		'CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','NMA','PO3CH5']

#ccs = ['HF','B3LYP','M06','MN15','WB97XD','MP2','CCSD']
ccs = ['B3LYP']

bs = list(nl.keys())

#output = {}
for mol in mols:
	for cc in ccs:
		#output[mol].append(cc)
		print('**********{:6s}**{:6s}***********'.format(mol,cc.lower()),file=output1)
		print('**********{:6s}**{:6s}***********'.format(mol,cc.lower()),file=output2)
		print('{:20s}'.format(''),end='',file=output1)
		print('{:20s}'.format(''),end='',file=output2)
		for x in range(0,len(bs)-1):
			print('{:>10s}'.format(bs[x]),end='',file=output1)
			print('{:>10s}'.format(bs[x]),end='',file=output2)
		print('',end='\n',file=output1)
		print('',end='\n',file=output2)
		for m in range(1,len(nl.keys())):
			print('{:>10s}/{:<10s} '.format(cc.lower(),bs[m]),end="",file=output1)
			print('{:>10s}/{:<10s} '.format(cc.lower(),bs[m]),end="",file=output2)
			for n in range(0,m):
				f1 = mol+'_'+cc.lower()+'_'+bs[m]+'.dat'
				f2 = mol+'_'+cc.lower()+'_'+bs[n]+'.dat'
				isf1 = os.path.exists(f1)
				isf2 = os.path.exists(f2)
				if isf1 and isf2:
                    # f2 as the reference data
					rmsd, rrmsd = ESP_rmsd(f1,f2)
					if isinstance(rmsd,float):
						print('{:10.5f}'.format(rmsd),end="",file=output1)
						print('{:10.5f}'.format(rmsd),end="",file=output2)
					else:
						print('{:>10s}'.format(rmsd),end="",file=output1)
						print('{:>10s}'.format(rmsd),end="",file=output2)
					#print(diff)
				else:
					print('{:>10s}'.format('noexist'),end="",file=output1)
					print('{:>10s}'.format('noexist'),end="",file=output2)
			print('',end="\n",file=output1)
			print('',end="\n",file=output2)
