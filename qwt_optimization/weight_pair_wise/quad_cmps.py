#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from utils.metrics import read_QM_quad, read_Fitted_quad
from utils.metrics import read_QM_dipole, read_Fitted_dipole
from utils.metrics import delta_mu, delta_Q

wks = [10**-5, 5*10**-5, 10**-4, 5*10**-4, 10**-3]
sts = [10**-5, 5*10**-5, 10**-4, 5*10**-4, 10**-3]

SMALL_MOLS = ['H2O','ClH','NH3','NH4+','CH4','CH2O','C2H2','C2H4','CH3Cl','CH3F','CH3OH','oh2oh2']
LARGE_MOLS = ['C2H6','C3H4','C3H8','C3N2H4','C3NOH3','C3NOH3p','C4H10','C4NH4','C4OH4','C5NH5','C6H6','CH3Br','CH3COCH3',\
				'CH3NH2','CH3OCH3','CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','NMA','PO3CH5']
				#'CH3NH2','CH3OCH3','CH3S2CH3','CH3SCH3','CH3SO2CH3','CHONH2','CHOOCH3','CHOOH','COCH3CH3','NMA','PO3CH5']

output1 = open('SMALL_Dipole_Quardpole_SUMMARY.txt','w')
output2 = open('LARGE_Dipole_Quardpole_SUMMARY.txt','w')


print('---SMALL SET ---')
for i,wk in enumerate(wks):
	for j,st in enumerate(sts):
		if i<j:
			delta_mu_total = []
			delta_Q_xx = []
			delta_Q_yy = []
			delta_Q_zz = []
			for small in SMALL_MOLS:
				if small != 'H2':
					path = 'small/{:7.6f}/{:7.6f}/{}/'.format(wk,st,small)
					fitted_out = path+small+'.2nd.out'
					path_gout = '../../../ESP/SMALL/ccsd/'+small+'_ccsd_a5z.log'
					# read quad fitted and QM derived
					quad_fitted = read_Fitted_quad(fitted_out)
					quad_qm_orig, quad_qm_diag = read_QM_quad(path_gout)
					# read dipole fitted and QM derived
					dipole_fitted = read_Fitted_dipole(fitted_out)
					dipole_qm     = read_QM_dipole(path_gout)
					#print('Fitted {}|{}|{}: {}'.format(wk,st,small,dipole_fitted))
					#print('QM | {}: {}'.format(small,dipole_qm))
					#print('Fitted {}|{}|{}: {}'.format(wk,st,small,quad_fitted))
					#print('QM |{}: {}'.format(small,quad_qm_diag))
					tmp_mu = delta_mu(dipole_qm, dipole_fitted)
					tmp_Q_xx = delta_Q(quad_qm_diag[0],quad_fitted[0])
					tmp_Q_yy = delta_Q(quad_qm_diag[1],quad_fitted[1])
					tmp_Q_zz = delta_Q(quad_qm_diag[2],quad_fitted[2])
					
					delta_mu_total.append(tmp_mu)
					delta_Q_xx.append(tmp_Q_xx)
					delta_Q_yy.append(tmp_Q_yy)
					delta_Q_zz.append(tmp_Q_zz)
	
			print('wk:{:7.6f}; st:{:7.6f}; Delta mu:{:10.4f} Q_xx:{:10.4f} Q_yy:{:10.4f} Q_zz:{:10.4f} Total_Q:{:10.4f}'.format(\
										wk,st,np.sqrt(sum(delta_mu_total)/len(delta_mu_total)),\
												np.sqrt(sum(delta_Q_xx)/len(delta_Q_xx)),\
												np.sqrt(sum(delta_Q_yy)/len(delta_Q_yy)),\
												np.sqrt(sum(delta_Q_zz)/len(delta_Q_zz)),\
												sum(delta_Q_xx)+sum(delta_Q_yy)+sum(delta_Q_zz)),file=output1)
		#print('wk:{:7.4f}; st:{:7.4f}; Delta mu:{:10.4f}'.format(wk,st,sum(delta_mu_total)/len(delta_mu_total)))
		#print('wk:{:7.6f}; st:{:7.6f}; Delta Q_xx:{:10.4f} Delta Q_yy:{:10.4f} Delta Q_zz:{:10.4f}'.format(wk,st,\
		#					sum(delta_Q_xx),\
		#					sum(delta_Q_yy),\
		#					sum(delta_Q_zz)))
							#sum(delta_Q_xx)/len(delta_Q_xx),\
							#sum(delta_Q_yy)/len(delta_Q_yy),\
							#sum(delta_Q_zz)/len(delta_Q_zz)))
			
print('---LARGE SET---')
for i,wk in enumerate(wks):
	for j,st in enumerate(sts):
		if i<j:
			delta_mu_total = []
			delta_Q_xx = []
			delta_Q_yy = []
			delta_Q_zz = []
			for large in LARGE_MOLS:
				if large != 'H2':
					#print(large)
					path = 'large/{:7.6f}/{:7.6f}/{}/'.format(wk,st,large)
					fitted_out = path+large+'.2nd.out'
					path_gout = '../../../ESP/LARGE/mp2/'+large+'_mp2_a5z.log'
					# read quad fitted and QM derived
					quad_fitted = read_Fitted_quad(fitted_out)
					quad_qm_orig, quad_qm_diag = read_QM_quad(path_gout)
					# read dipole fitted and QM derived
					dipole_fitted = read_Fitted_dipole(fitted_out)
					dipole_qm     = read_QM_dipole(path_gout)
					#print('Fitted {}|{}|{}: {}'.format(wk,st,small,dipole_fitted))
					#print('QM | {}: {}'.format(small,dipole_qm))
					#print('Fitted {}|{}|{}: {}'.format(wk,st,small,quad_fitted))
					#print('QM |{}: {}'.format(small,quad_qm_diag))
					tmp_mu = delta_mu(dipole_qm, dipole_fitted)
					tmp_Q_xx = delta_Q(quad_qm_diag[0],quad_fitted[0])
					tmp_Q_yy = delta_Q(quad_qm_diag[1],quad_fitted[1])
					tmp_Q_zz = delta_Q(quad_qm_diag[2],quad_fitted[2])
					
					delta_mu_total.append(tmp_mu)
					delta_Q_xx.append(tmp_Q_xx)
					delta_Q_yy.append(tmp_Q_yy)
					delta_Q_zz.append(tmp_Q_zz)
	
			print('wk:{:7.6f}; st:{:7.6f}; Delta mu:{:10.4f} Q_xx:{:10.4f} Q_yy:{:10.4f} Q_zz:{:10.4f} Total_Q:{:10.4f}'.format(\
										wk,st,np.sqrt(sum(delta_mu_total)/len(delta_mu_total)),\
												np.sqrt(sum(delta_Q_xx)/len(delta_Q_xx)),\
												np.sqrt(sum(delta_Q_yy)/len(delta_Q_yy)),\
												np.sqrt(sum(delta_Q_zz)/len(delta_Q_zz)),\
												sum(delta_Q_xx)+sum(delta_Q_yy)+sum(delta_Q_zz)),file=output2)
