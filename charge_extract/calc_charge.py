#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import glob
from espdiff.goututils import readcharge
import os

# mapping the abbreviation to the full-length name
nl = {'321g':'3-21G','321pg':'3-21+G','631g':'6-31G*',\
		'631gss':'6-31++g**','6311g':'6311++G**',\
		'2z':'cc-pvdz','a2z':'aug-cc-pvdz','3z':'cc-pvtz',\
		'a3z':'aug-cc-pvtz','4z':'cc-pvqz','a4z':'aug-cc-pvqz',\
		'5z':'cc-pv5z','a5z':'aug-cc-pv5z'}

MOL_s = ['H2O','ClH','NH3','NH4+','CH4','CH2O','C2H2','C2H4','CH3Cl','CH3F','CH3OH','oh2oh2']
MOL_l = ['C2H6','C3H4','C3H8','C3N2H4','C3NOH3','C3NOH3p','C4H10','C4NH4','C4OH4','C5NH5','C6H6','CH3Br','CH3COCH3',\
		'CH3NH2','CH3OCH3','CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','NMA','PO3CH5']

ccs = ['B3LYP']

output = open('CHARGE_SUMMARY.txt','w')
output1 = open('FORMAT2TEX.txt','w')

total_charge = {}

for mol in MOL_l:
	print('******{:6s}******'.format(mol),file=output)
	total_charge['{}'.format(mol)] = {}
	for cc in ccs:
		for bs_abb, bs_v in nl.items():
			fname = '../'+mol+'_'+cc.lower()+'_'+bs_abb+'.log'
			total_charge['{}'.format(mol)]['{}'.format(bs_abb)] = {}
			isfname = os.path.exists(fname)
			if isfname:
				charge = readcharge(fname,mode='esp')
				
				print('{:>8s}'.format(''),end='',file=output)
				for i_elem,elem in enumerate(charge['elem']):
					total_charge['{}'.format(mol)]['{}'.format(bs_abb)]['{}'.format(i_elem)] = []
					print('{:>9s} '.format(elem),end='',file=output)
				print('',end='\n',file=output)

				print('{:8s} '.format(bs_abb),end='',file=output)

				for i_q, q in enumerate(charge['q']):
					print('{:9.3f} '.format(q),end='',file=output)
					total_charge['{}'.format(mol)]['{}'.format(bs_abb)]['{}'.format(i_q)].append(q)
				print('',end='\n',file=output)


		#print(total_charge['{}'.format(mol)])
		print('******{:6s}******'.format(mol),file=output1)
		#print('{:>8s}'.format(''),end='',file=output1)
		for bs_abb, bs_v in nl.items():
			print('{:>9s} '.format(bs_abb),end='',file=output1)
		print('',end='\n',file=output1)
		data = pd.DataFrame(data=total_charge['{}'.format(mol)])
		#print(data)
		for i in range(data.shape[0]):
			print('{}&'.format(charge['elem'][i]),end='',file=output1)
			for j in range(data.shape[1]):
				try:
					print('{:9.3f}&'.format(data.iloc[i,j][0]),end='',file=output1)
				except:
					print('{:>9s}&'.format('-'),end='',file=output1)
			print('',end='\n',file=output1)
		#total_charge['{}'.format(mol)] = pd.DataFrame(data=total_charge['{}'.format(mol)],columns=nl.keys(),index=charge['elem'])
		#print(total_charge['{}'.format(mol)])

				#for elem,q in zip(charge['elem'],charge['q']):
				#	total_charge[mol][elem].append(q)
					
				#total_charge[mol].append(charge['q'])
				#print(charge)
#print(total_charge['CH3Br']['321pg'])
#-------------------------#
# Section for rms and rrms#
#-------------------------#
fmt_data = {}
for bs_abb, bs_v in nl.items():
    fmt_data['{}'.format(bs_abb)] = []
    for mol in MOL_l:
        if len(total_charge['{}'.format(mol)]['{}'.format(bs_abb)]):
            for elem_i, charges in total_charge['{}'.format(mol)]['{}'.format(bs_abb)].items():
                fmt_data['{}'.format(bs_abb)].append(charges[0])
        else:
            for elem_i, charges in total_charge['{}'.format(mol)]['a5z'].items():
                fmt_data['{}'.format(bs_abb)].append('x')
#
#print(fmt_data['321pg'])

rms = []
rrms = []
for bs_abb, bs_v in nl.items():
    if bs_abb != 'a5z':
        ssd = 0
        r1  = 0
        r2  = 0
        num = 0
        for i,v in enumerate(fmt_data['{}'.format(bs_abb)]):
            if v != 'x':
                ssd += (fmt_data['{}'.format(bs_abb)][i] - fmt_data['a5z'][i])**2
                num+=1
                r1  += fmt_data['a5z'][i]**2
        rms_tmp = (ssd/num)**0.5
        rrms_tmp = (ssd/r1)**0.5
        #rms_tmp = (sum((np.array(fmt_data['{}'.format(bs_abb)]) - np.array(fmt_data['a5z']))**2)/len(fmt_data['a5z']))**0.5
        #rrms_tmp = rms_tmp / (sum(np.array(fmt_data['a5z'])**2)/len(fmt_data['a5z']))**0.5

        rms.append(rms_tmp)
        rrms.append(rrms_tmp)
        print('{:>9s} '.format(bs_abb),end='',file=output1)
print('',end='\n',file=output1)  

print('{}'.format('rms &'), end='',file=output1)
for x_rms in rms:
    print('{:9.3f}&'.format(x_rms),end='',file=output1)
print('',end='\n',file=output1)

print('{}'.format('rrms &'), end='',file=output1)
for x_rrms in rrms:
    print('{:7.2f}\%&'.format(x_rrms*100),end='',file=output1)
print('',end='\n',file=output1)
#print(rms,rrms)

