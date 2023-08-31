#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
import glob
from utils.pgm_exe import pyresp_gen,polresp_exe, pyresp_exe
from utils.metrics import rrms
from utils.metrics import read_Fitted_esp
import shutil

#constraints = [10**-5, 10**-4, 10**-3, 5*10**-3, 10**-2, 5*10**-2, 10**-1,5*10**-1,10**0,5,10,100]

wks = [10**-5, 5*10**-5, 10**-4, 5*10**-4, 10**-3]
sts = [10**-5, 5*10**-5, 10**-4, 5*10**-4, 10**-3]

SMALL_MOLS = ['H2O','ClH','NH3','NH4+','CH4','CH2O','C2H2','C2H4','CH3Cl','CH3F','CH3OH','oh2oh2']
LARGE_MOLS = ['C2H6','C3H4','C3H8','C3N2H4','C3NOH3','C3NOH3p','C4H10','C4NH4','C4OH4','C5NH5','C6H6','CH3Br','CH3COCH3',\
			'CH3NH2','CH3OCH3','CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','NMA','PO3CH5']
				#'CH3NH2','CH3OCH3','CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','COCH3CH3','NMA','PO3CH5']

output1 = open('SMALL_PAIRED_SUMMARY.txt','w')
output2 = open('LARGE_PAIRED_SUMMARY.txt','w')

def mkdir(path):
	isExists = os.path.exists(path)
	
	if not isExists:
		os.makedirs(path)
	else:
		# remove the previous ones
		shutil.rmtree(path)
		# create the new one
		os.makedirs(path)

#print('#----Two-Stage Test----#')

for i,wk in enumerate(wks):
	for j,st in enumerate(sts):
		if i < j:
			for small in SMALL_MOLS:
				path = 'small/{:7.6f}/{:7.6f}/{}/'.format(wk,st,small)
				# mkdir according to path specifed
				mkdir(path)
				espdat = '../../SMALL/ccsd/'+small+'_ccsd_a5z.dat'
				f1name = path+small+'.1st'
				f2name = path+small+'.2nd'
				if small == 'NH4+':
					pyresp_gen(espdat,f1name,f2name,1,wk,st,'ind')
					# exe 1st stage estimation
					pyresp_exe(f1name,f2name,espdat,1)
					# exe 2nd stage estimation
					pyresp_exe(f1name,f2name,espdat,2)
				else:
					# generating the input file
					pyresp_gen(espdat,f1name,f2name,0,wk,st,'ind')
					# exe 1st stage estimation
					pyresp_exe(f1name,f2name,espdat,1)
					# exe 2nd stage estimation
					pyresp_exe(f1name,f2name,espdat,2)
   		
print('---SMALL SET---')
for i,wk in enumerate(wks):
	for j,st in enumerate(sts):
		if i<j:
			rrms_total = []
			for small in SMALL_MOLS:
				if small !='H2':
					path = 'small/{:7.6f}/{:7.6f}/{}/'.format(wk,st,small)
					f_fit_esp = path+small+'.2nd.esp'
					esp_qm, esp_fit = read_Fitted_esp(f_fit_esp)
					tmp = rrms(esp_qm,esp_fit)
					rrms_total.append(tmp)
			print('wk:{:7.6f}; st:{:7.6f}; Total RRMS:{:10.4f}; Dev:{:10.4f}'.format(wk,st,np.mean(rrms_total),np.std(rrms_total)),file=output1)
#

for i,wk in enumerate(wks):
	for j,st in enumerate(sts):
		if i < j:
			for large in LARGE_MOLS:
				path = 'large/{:7.6f}/{:7.6f}/{}/'.format(wk,st,large)
				# mkdir according to path specifed
				mkdir(path)
				espdat = '../../LARGE/mp2/'+large+'_mp2_a5z.dat'
				f1name = path+large+'.1st'
				f2name = path+large+'.2nd'
				if large == 'NH4+':
					pyresp_gen(espdat,f1name,f2name,1,wk,st,'ind')
				else:
					# generating the input file
					pyresp_gen(espdat,f1name,f2name,0,wk,st,'ind')
					# exe 1st stage estimation
					pyresp_exe(f1name,f2name,espdat,1)
					# exe 2nd stage estimation
					pyresp_exe(f1name,f2name,espdat,2)

print('---LARGE SET---')			
for i,wk in enumerate(wks):
	for j,st in enumerate(sts):
		if i< j:
			rrms_total = []
			for large in LARGE_MOLS:
				path = 'large/{:7.6f}/{:7.6f}/{}/'.format(wk,st,large)
				f_fit_esp = path+large+'.2nd.esp'
				esp_qm, esp_fit = read_Fitted_esp(f_fit_esp)
				tmp = rrms(esp_qm,esp_fit)
				rrms_total.append(tmp)
			#print('wk:{:7.6f}; st:{:7.6f}; Total RRMS:{:10.4f}'.format(wk,st,sum(rrms_total)/len(rrms_total)))
			print('wk:{:7.6f}; st:{:7.6f}; Total RRMS:{:10.4f}; Dev:{:10.4f}'.format(wk,st,np.mean(rrms_total),np.std(rrms_total)),file=output2)




if __name__ == '__main__':
	pass
