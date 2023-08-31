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
					esp_xyz.append([float(line.split()[1]), float(line.split()[2]),float(line.split()[3])])
	xyz = np.array(xyz)
	esp = np.array(esp)
	esp_xyz = np.array(esp_xyz)

	return num, ngrid, xyz, esp, esp_xyz

def sortesp(esp, esp_xyz):
	"""
	input:
		read the esp data extracted from func: readesp
	function:
		sort the esp data point in a descending order
	return num, ngrid, xyz, esp, esp_xyz
	"""
	output = {'espv':[],'esp_x':[],'esp_y':[],'esp_z':[]}
	output['espv'] = esp
	output['esp_x'] = esp_xyz[:,0]
	output['esp_y'] = esp_xyz[:,1]
	output['esp_z'] = esp_xyz[:,2]

	output = pd.DataFrame(output)
	
	output_sort = output.sort_values(['esp_x','esp_y','esp_z'],ascending=[True,True,True])

	return output_sort['espv'].values, output_sort[['esp_x','esp_y','esp_z']].values
	

def ESPdiff(f1,f2):
	sd = 0
	ssd =0
	r1 = 0
	r2 = 0
	s1 = 0
	s2 = 0
	num1, ngrid1,xyz1, esp1, esp_xyz1 = readesp(f1)
	num2, ngrid2,xyz2, esp2, esp_xyz2 = readesp(f2)
	
	esp1_sort, esp_xyz1_sort = sortesp(esp1,esp_xyz1)
	esp2_sort, esp_xyz2_sort = sortesp(esp2,esp_xyz2)

	#print(esp_xyz1_sort)
	#print(esp_xyz2_sort)
	
	if ngrid1 != ngrid2:
		diff = 'nomatch'
	else:
		for i in range(ngrid1):
			sd +=esp1_sort[i] - esp2_sort[i]
			ssd+=(esp1_sort[i] - esp2_sort[i])**2
			r1 +=esp1_sort[i]**2
			r2 +=esp2_sort[i]**2
			s1 +=esp1_sort[i]
			s2 +=esp2_sort[i]

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

def ESP_rmsd(f1,f2):
    '''
    f1: queried one
    f2: referenced one
    '''
    ssd = 0
    r1 = 0
    r2 = 0
    num1, ngrid1,xyz1, esp1, esp_xyz1 = readesp(f1)
    num2, ngrid2,xyz2, esp2, esp_xyz2 = readesp(f2)

    esp1_sort, esp_xyz1_sort = sortesp(esp1,esp_xyz1)
    esp2_sort, esp_xyz2_sort = sortesp(esp2,esp_xyz2)

    if ngrid1 != ngrid2:
        diff = 'nomatch'
    else:
        for i in range(ngrid1):
            ssd+=(esp1_sort[i] - esp2_sort[i])**2
            r1 +=esp1_sort[i]**2
            r2 +=esp2_sort[i]**2

        ssd = ssd/ngrid1
        r1  = r1/ngrid1
        r2  = r2/ngrid2

        rmsd = ssd**0.5
        rrmsd= rmsd/r2**0.5

    return rmsd, rrmsd




if __name__ == '__main__':
	filename = '../ClH_m062x_321g_esp.dat'
	num, ngrid, xyz, esp, esp_xyz = readesp(filename)
	print("number of atoms: {:3d}".format(num))
	print("number of grid points: {:5d}".format(ngrid))
	print(xyz)
	print(esp)
	print(esp_xyz)
	
	f1 = '../ClH_m062x_321g_esp.dat'
	f2 = '../../../CCSD/esp/ClH_ccsd_a5z_esp.dat'
	diff12 = ESPdiff(f1,f2)
	print("Difference between two esp data is {:10.6f}".format(diff12))
