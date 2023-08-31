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



if __name__ == '__main__':
	filename = 'CH2O.1st.esp'
	esp_qm, esp_fit = read_Fitted_esp(filename)
	
	rrms_ele = rrms(esp_qm, esp_fit)
	print(rrms_ele)
	#print(esp_qm)
	#print(esp_fit)
