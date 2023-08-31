#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def readbs(fn):
	with open(fn,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if 'basis functions,' in line:
					bs = int(line.split()[0])
	return bs

def readcharge(fn,mode='mulliken'):
	charge = {'elem':[],'q':[]}
	with open(fn,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if mode == 'mulliken':
					if 'Mulliken charges:' in line:
						line = f.readline()
						for i in range(999):
							line = f.readline()
							if 'Sum of Mulliken charges =' in line:
								break
							else:
								charge['elem'].append(line.split()[1])
								charge['q'].append(float(line.split()[2]))
				elif mode == 'esp':
					if 'ESP charges:' in line:
						line = f.readline()
						for i in range(999):
							line = f.readline()
							if 'Sum of ESP charges =' in line:
								break
							else:
								charge['elem'].append(line.split()[1])
								charge['q'].append(float(line.split()[2]))

	return charge



def BSdiff(f1,f2):
	bs1 = readbs(f1)
	bs2 = readbs(f2)
	return bs1-bs2

if __name__ == '__main__':
	fn = '../C2H2_b3lyp_a2z_esp.gout'
	bs = readbs(fn)
	print('Basis set: {:5d}'.format(bs))
	charge = readcharge(fn,mode='mulliken')
	print(charge)


