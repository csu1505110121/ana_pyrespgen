#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def dump_opt(filename,mol,xyz,charge=0,spin=1):
	with open(filename,'w') as f:
		f.write('%chk={}_mp2.chk\n'.format(mol))
		f.write('%nproc=4\n')
		f.write('%mem=10Gb\n')
		f.write('# opt mp2/6-311++g(d,p)\n')
		f.write('\n')
		f.write('opt {}\n'.format(mol))
		f.write('\n')
		f.write('{} {}\n'.format(charge,spin))
		for i in range(xyz.shape[0]):
			f.write('{} {:10.5f} {:10.5f} {:10.5f}\n'.format(xyz.iloc[i]['ATYPE'],\
													xyz.iloc[i]['x'],\
													xyz.iloc[i]['y'],\
													xyz.iloc[i]['z']))
		f.write('\n')
		f.write('\n')
	




if __name__ == '__main__':
	pass
