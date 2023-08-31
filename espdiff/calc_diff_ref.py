#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import glob
from espdiff.esputils import ESP_rmsd
import os

output1 = open('ESP_RMSD.txt','w')
output2 = open('ESP_RRMSD.txt','w')

# mapping the abbreviation to the full-length name
nl = {'321g':'3-21G','321pg':'3-21+G','631g':'6-31G*',\
		'631gss':'6-31++g**','6311g':'6311++G**',\
		'2z':'cc-pvdz','a2z':'aug-cc-pvdz','3z':'cc-pvtz',\
		'a3z':'aug-cc-pvtz','4z':'cc-pvqz','a4z':'aug-cc-pvqz',\
		'5z':'cc-pv5z','a5z':'aug-cc-pv5z'}

mols = ['C2H6','C3H4','C3H8','C3N2H4','C3NOH3','C3NOH3p','C4H10',\
		'C4NH4','C4OH4','C5NH5','C6H6','CH3Br','CH3COCH3','CH3NH2','CH3OCH3',\
		'CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','NMA','PO3CH5']
		#'CH3S2CH3','CH3SCH3','CH3SO2CH3','CHNHOH','CHOOCH3','CHOOH','COCH3CH3','NMA','PO3CH5']

#ccs = ['HF','B3LYP','M06','MN15','WB97XD','MP2','CCSD']
ccs = ['B3LYP']

refn = 'mp2'
refbs = ['a5z']

bs = list(nl.keys())

# taking the reference basis set in the following order:
#   - aug-cc-pv5z
#   - cc-pv5z
#   - aug-cc-pvqz
#   - cc-pvqz
for mol in mols:
	for rb in refbs:
		fref = '../'+refn.lower()+'/'+mol+'_'+refn+'_'+rb+'.dat'
		if os.path.exists(fref):
			break
	#print(rb)
	for cc in ccs:
		print('**********{:6s}**{:6s}***********'.format(mol,cc.lower()),file=output1)
		print('**********{:6s}**{:6s}***********'.format(mol,cc.lower()),file=output2)
		print('{:20s}'.format(''),end='',file=output1)
		print('{:20s}'.format(''),end='',file=output2)
		for x in range(0,len(bs)):
			print('{:>10s}'.format(bs[x]),end='',file=output1)
			print('{:>10s}'.format(bs[x]),end='',file=output2)
		print('',end='\n',file=output1)
		print('',end='\n',file=output2)
		#print('test',end='')
		print('{:>10s}/{:<10s} '.format(refn,rb),end='',file=output1)
		print('{:>10s}/{:<10s} '.format(refn,rb),end='',file=output2)
		for m in range(0,len(bs)):
			f1 = mol+'_'+cc.lower()+'_'+bs[m]+'.dat'
			if os.path.exists(f1):
				rmsd, rrmsd = ESP_rmsd(f1,fref)
				if isinstance(rmsd,float):
					print('{:10.5f}'.format(rmsd),end="",file=output1)
					print('{:10.5f}'.format(rrmsd),end="",file=output2)
				else:
					print('{:>10s}'.format(rmsd),end="",file=output1)
					print('{:>10s}'.format(rrmsd),end="",file=output2)
			else:
				print('{:>10s}'.format('noexist'),end="",file=output1)
				print('{:>10s}'.format('noexist'),end="",file=output2)
	print('',end="\n",file=output1)
	print('',end="\n",file=output2)
		
		

