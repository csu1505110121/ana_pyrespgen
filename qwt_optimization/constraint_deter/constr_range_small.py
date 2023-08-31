#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
import glob
from utils.pgm_exe import pyresp_gen, polresp_exe
from utils.metrics import rrms
from utils.metrics import read_Fitted_esp
import shutil

constraints = [10**-5, 10**-4, 10**-3, 5*10**-3, 10**-2, 5*10**-2, 10**-1,5*10**-1,10**0,5,10,100]

SMALL_MOLS = ['H2O','ClH','NH3','NH4+','CH4','CH2O','C2H2','C2H4','CH3Cl','CH3F','CH3OH','oh2oh2']
LARGE_MOLS = ['C2H6','C3H4','C3H8','C3N2H4','C3NOH3','C3NOH3p','C4H10','C4NH4','C4OH4','C5NH5','C6H6','CH3Br','CH3COCH3',\
			'CH3NH2','CH3OCH3','CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','NMA','PO3CH5']
			#'CH3NH2','CH3OCH3','CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','COCH3CH3','NMA','PO3CH5']

output = open('SMALL_RRMS_SUMMARY.txt','w')

def mkdir(path):
	isExists = os.path.exists(path)
	
	if not isExists:
		os.makedirs(path)
	else:
		# remove the previous ones
		shutil.rmtree(path)
		# create the new one
		os.makedirs(path)

#print('----SMALL SET ----')
#for ctr in constraints:
#	#print(ctr)
#	rrms_total = []
#	for small in SMALL_MOLS:
#		path = 'small/{:7.6f}/{}/'.format(ctr,small)
#		mkdir(path)
#		espdat = '../../SMALL/ccsd/'+small+'_ccsd_a5z.dat'
#		f1name = path+small+'.{:7.6f}.1st'.format(ctr)
#		if small == 'NH4+':
#			#print(small,ctr)
#			pyresp_gen(espdat,f1name,ctr,1)
#			polresp_exe(path+small,ctr,espdat)
#		else:
#			pyresp_gen(espdat,f1name,ctr,0)
#			polresp_exe(path+small,ctr,espdat)
#			#f_fit_esp = path+large+'.{:7.6f}.1st.esp'.format(ctr)
#			#esp_qm, esp_fit = read_Fitted_esp(f_fit_esp)
#			#tmp = rrms(esp_qm,esp_fit)
#			#rrms_total.append(tmp)
#	#print('Constraint: {:7.6f}; Total RRMS: {:10.7f}'.format(ctr,sum(rrms_total)))

print('----SMALL SET----')
for ctr in constraints:
	rrms_total = []
	for small in SMALL_MOLS:
		path = 'small/{:7.6f}/{}/'.format(ctr,small)
		f_fit_esp = path+small+'.{:7.6f}.1st.esp'.format(ctr)
		esp_qm,esp_fit = read_Fitted_esp(f_fit_esp)
		tmp = rrms(esp_qm,esp_fit)
		rrms_total.append(tmp)

	print('Constraint: {:6.5f}; Total RRMS: {:10.7f}'.format(ctr,sum(rrms_total)/len(rrms_total)),file=output)



if __name__ == '__main__':
	pass
