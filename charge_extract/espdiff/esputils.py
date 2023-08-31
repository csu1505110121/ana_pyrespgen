#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import math


def readesp(fesp):
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

def ESPdiff(f1,f2):
	sd = 0
	ssd =0
	r1 = 0
	r2 = 0
	s1 = 0
	s2 = 0
	num1, ngrid1,xyz1, esp1, esp_xyz1 = readesp(f1)
	num2, ngrid2,xyz2, esp2, esp_xyz2 = readesp(f2)
	if ngrid1 != ngrid2:
		diff = 'nomatch'
	else:
		for i in range(ngrid1):
			sd +=esp1[i] - esp2[i]
			ssd+=(esp1[i] - esp2[i])**2
			r1 +=esp1[i]**2
			r2 +=esp2[i]**2
			s1 +=esp1[i]
			s2 +=esp2[i]

		sd = sd/ngrid1
		ssd = ssd/ngrid1
		r1 = r1/ngrid1
		r2 = r2/ngrid2
		s1 = s1/ngrid1
		s2 = s2/ngrid2
	
		ssd -=sd*sd
		r1 -=s1*s1
		r2 -=s2*s2

		diff = ssd**0.5/(0.5*(r1+r2))**0.5
	return diff




if __name__ == '__main__':
	filename = '../C2H2_b3lyp_2z_esp.dat'
	num, ngrid, xyz, esp, esp_xyz = readesp(filename)
	print("number of atoms: {:3d}".format(num))
	print("number of grid points: {:5d}".format(ngrid))
	print(xyz)
	print(esp)
	print(esp_xyz)
	
	f1 = '../C2H2_b3lyp_2z_esp.dat'
	f2 = '../C2H2_b3lyp_3z_esp.dat'
	diff12 = ESPdiff(f1,f2)
	print("Difference between two esp data is {:10.6f}".format(diff12))
