#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import math

def rrms(v_qm,v_fit):
	#rrms = 0
	delta = 0
	qm2 = 0
	if len(v_qm) == len(v_fit):
		for i in range(len(v_qm)):
			qm2 += v_qm[i]**2
			delta += (v_qm[i] - v_fit[i])**2
		rrms = math.sqrt(delta / qm2)
		return rrms
	else:
		rrms = 'error'
		return rrms

def delta_mu(mu_qm,mu_fit):
	delta2 = (mu_qm - mu_fit)**2
	return delta2

def delta_Q(Q_qm, Q_fit):
	delta2 = (Q_qm - Q_fit)**2
	return delta2


def read_QM_esp(fesp):
	'''
	- input:
	read the esp format file
	- output:
	#arg1: number of atoms
	#arg2: number of esp grid
	#arg3: xyz of molecule
	#arg4: xyz of grid point
	'''
	xyz = []
	esp = []
	esp_xyz = []
	with open(fesp) as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				num =int(line[:5])
				ngrid = int(line[5:10])
				for i in range(num):
					line = f.readline()
					xyz.append([float(line.split()[a]) for a in range(3)]) # in case the atom type is defined here
				for i in range(ngrid):
					line = f.readline()
					esp.append(float(line.split()[0]))
					esp_xyz.append([float(x) for x in line.split()])
	xyz = np.array(xyz)
	esp = np.array(esp)
	esp_xyz = np.array(esp_xyz)

	return num, ngrid, xyz, esp, esp_xyz

def read_Fitted_esp(fesp):
	esp_qm = []
	esp_fit = []
	with open(fesp) as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if 'esp_qm' in line:
					for i in range(9999999)	:
						line = f.readline()
						if 'molecule' in line:
							break
						else:
							esp_qm.append(float(line.split()[3]))
							esp_fit.append(float(line.split()[4]))

	return esp_qm, esp_fit

def read_QM_quad(gout):
	quad_orig = np.ndarray((3,3))
	with open(gout,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if 'Traceless Quadrupole moment (field-independent basis, Debye-Ang)' in line:
					line = f.readline()
					quad_orig[0][0] = float(line.split()[1])
					quad_orig[1][1] = float(line.split()[3])
					quad_orig[2][2] = float(line.split()[5])
					line = f.readline()
					quad_orig[0][1] = float(line.split()[1])
					quad_orig[1][0] = float(line.split()[1])
					quad_orig[0][2] = float(line.split()[3])
					quad_orig[2][0] = float(line.split()[3])
					quad_orig[1][2] = float(line.split()[5])
					quad_orig[2][1] = float(line.split()[5])

	quad_diag, vec = np.linalg.eigh(quad_orig)
	quad_diag = sorted(quad_diag, reverse=True)
	return quad_orig, quad_diag

def read_QM_dipole(gout):
	with open(gout,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if 'Dipole moment (field-independent basis, Debye):' in line:
					line = f.readline()
					dipole = float(line.split()[7])
					return dipole

def read_Fitted_dipole(fitted_out):
	with open(fitted_out,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if 'Dipole Moments (Debye):' in line:
					line = f.readline() # skip '#MOL D Dx Dy Dz'
					line = f.readline()
					dipole = float(line.split()[1])
					return dipole
					


def read_Fitted_quad(fitted_out):
	quad_diag = []
	with open(fitted_out,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if 'Traceless Quadrupole Moments in Principal Axes (Debye*Angst.):' in line:
					line = f.readline() # skipping the line "MOL X Y Z"
					line = f.readline()
					quad_diag.append(float(line.split()[2]))
					line = f.readline()
					quad_diag.append(float(line.split()[2]))
					line = f.readline()
					quad_diag.append(float(line.split()[3]))
	return quad_diag
					






if __name__ == '__main__':
	filename = 'CH2O.1st.esp'
	esp_qm, esp_fit = read_Fitted_esp(filename)
	
	rrms_ele = rrms(esp_qm, esp_fit)
	print(rrms_ele)
	#print(esp_qm)
	#print(esp_fit)
