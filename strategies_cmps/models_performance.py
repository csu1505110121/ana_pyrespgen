#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
import glob
from utils.metrics import rrms
from utils.metrics import read_Fitted_esp
from utils.metrics import read_QM_quad, read_Fitted_quad
from utils.metrics import read_QM_dipole, read_Fitted_dipole
from utils.metrics import delta_mu, delta_Q
import shutil

#SMALL_MOLS = ['H2O','ClH','NH3','NH4+','CH4','CH2O','C2H2','C2H4','CH3Cl','CH3F','CH3OH','oh2oh2']
SMALL_MOLS = ['CH4','CH3Cl','CH3F','CH3OH']
LARGE_MOLS = ['C2H6','C3H8','C4H10','CH3Br','CH3COCH3',\
				'CH3NH2','CH3OCH3','CH3S2CH3','CH3SCH3','CH3SO2CH3','CHOOCH3','NMA','PO3CH5']

output = open('performance_summary.txt','w')

rrms_total_small = []
for small in SMALL_MOLS:
	path = 'small/{0}/5resp-perm/'.format(small)
	f_fit_esp = path+small+'.2nd.esp'
	esp_qm, esp_fit = read_Fitted_esp(f_fit_esp)
	tmp = rrms(esp_qm, esp_fit)
	rrms_total_small.append(tmp)

print('Strategy I | Total RRMS over SMALL: {:10.4f}'.format(sum(rrms_total_small)/len(rrms_total_small)),file=output)

rrms_total_large = []
for large in LARGE_MOLS:
	path = 'large/{0}/5resp-perm/'.format(large)
	f_fit_esp = path+large+'.2nd.esp'
	esp_qm, esp_fit = read_Fitted_esp(f_fit_esp)
	tmp = rrms(esp_qm, esp_fit)
	rrms_total_large.append(tmp)

print('Strategy I | Total RRMS over LARGE: {:10.4f}'.format(sum(rrms_total_large)/len(rrms_total_large)),file=output)

delta_mu_small = []
delta_Q_xx_small = []
delta_Q_yy_small = []
delta_Q_zz_small = []
for small in SMALL_MOLS:
	path = 'small/{0}/5resp-perm/'.format(small)
	fitted_out = path+small+'.2nd.out'
	path_gout = '/home/zhuqiang/Documents/WorkHotel/pyresp/230419_self_construct/ESP/SMALL/ccsd/{0}_ccsd_a5z.log'.format(small)
	# read quad fitted and QM derived
	quad_fitted = read_Fitted_quad(fitted_out)
	quad_qm_orig, quad_qm_diag = read_QM_quad(path_gout)
	# read dipole fitted and QM derived
	dipole_fitted = read_Fitted_dipole(fitted_out)
	#print(small,dipole_fitted)
	dipole_qm     = read_QM_dipole(path_gout)
	tmp_mu = delta_mu(dipole_qm, dipole_fitted)
	tmp_Q_xx = delta_Q(quad_qm_diag[0],quad_fitted[0])
	tmp_Q_yy = delta_Q(quad_qm_diag[1],quad_fitted[1])
	tmp_Q_zz = delta_Q(quad_qm_diag[2],quad_fitted[2])
	
	delta_mu_small.append(tmp_mu)
	delta_Q_xx_small.append(tmp_Q_xx)
	delta_Q_yy_small.append(tmp_Q_yy)
	delta_Q_zz_small.append(tmp_Q_zz)

print('Strategy I SMALL set | Delta mu:{:10.4f} Q_xx:{:10.4f} Q_yy:{:10.4f} Q_zz:{:10.4f}'.format(np.sqrt(sum(delta_mu_small)/len(delta_mu_small)),\
						np.sqrt(sum(delta_Q_xx_small)/len(delta_Q_xx_small)),\
						np.sqrt(sum(delta_Q_yy_small)/len(delta_Q_yy_small)),\
						np.sqrt(sum(delta_Q_zz_small)/len(delta_Q_zz_small))),file=output)

delta_mu_large = []
delta_Q_xx_large = []
delta_Q_yy_large = []
delta_Q_zz_large = []
for large in LARGE_MOLS:
	path = 'large/{0}/5resp-perm/'.format(large)
	fitted_out = path+large+'.2nd.out'
	path_gout = '/home/zhuqiang/Documents/WorkHotel/pyresp/230419_self_construct/ESP/LARGE/mp2/{0}_mp2_a5z.log'.format(large)
	# read quad fitted and QM derived
	quad_fitted = read_Fitted_quad(fitted_out)
	quad_qm_orig, quad_qm_diag = read_QM_quad(path_gout)
	# read dipole fitted and QM derived
	dipole_fitted = read_Fitted_dipole(fitted_out)
	#print(small,dipole_fitted)
	dipole_qm     = read_QM_dipole(path_gout)
	tmp_mu = delta_mu(dipole_qm, dipole_fitted)
	tmp_Q_xx = delta_Q(quad_qm_diag[0],quad_fitted[0])
	tmp_Q_yy = delta_Q(quad_qm_diag[1],quad_fitted[1])
	tmp_Q_zz = delta_Q(quad_qm_diag[2],quad_fitted[2])
	
	delta_mu_large.append(tmp_mu)
	delta_Q_xx_large.append(tmp_Q_xx)
	delta_Q_yy_large.append(tmp_Q_yy)
	delta_Q_zz_large.append(tmp_Q_zz)

print('Strategy I LARGE set | Delta mu:{:10.4f} Q_xx:{:10.4f} Q_yy:{:10.4f} Q_zz:{:10.4f}'.format(np.sqrt(sum(delta_mu_large)/len(delta_mu_large)),\
						np.sqrt(sum(delta_Q_xx_large)/len(delta_Q_xx_large)),\
						np.sqrt(sum(delta_Q_yy_large)/len(delta_Q_yy_large)),\
						np.sqrt(sum(delta_Q_zz_large)/len(delta_Q_zz_large))),file=output)
