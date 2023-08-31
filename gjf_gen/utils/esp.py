#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def dump_esp(filename,mol,xyz,bs_abb,bs,method,charge=0,spin=1):
	with open(filename,'w') as f:
		f.write('%chk={}_{}_{}.chk\n'.format(mol,method,bs_abb))
		f.write('%nproc=40\n')
		f.write('%mem=120Gb\n')
		f.write('#{}/{}\n'.format(method,bs))
		f.write('#SCF=tight\n')
		f.write('#maxdisk=400Gb\n')
		f.write('#Pop=MK iop(6/33=2) iop(6/42=6) iop(6/43=20)\n')
		f.write('#IOP(5/87=12)\n')
		f.write('#density=current\n')
		f.write('\n')
		f.write('ESP det {} | {}/{}\n'.format(mol,method,bs))
		f.write('\n')
		f.write('{} {}\n'.format(charge,spin))
		for i in range(len(xyz['elem'])):
			f.write('{} {:10.5f} {:10.5f} {:10.5f}\n'.format(xyz['elem'][i],\
									xyz['x'][i],xyz['y'][i],xyz['z'][i]))
		f.write('\n')
		f.write('\n')

def dump_esp_gen(filename,mol,xyz,bs_abb,bs,method,charge=0,spin=1):
	with open(filename,'w') as f:
		f.write('%chk={}_{}_{}.chk\n'.format(mol,method,bs_abb))
		f.write('%nproc=40\n')
		f.write('%mem=80Gb\n')
		f.write('#{}/{}\n'.format(method,bs))
		f.write('#SCF=tight\n')
		f.write('#maxdisk=400Gb\n')
		f.write('#Pop=MK iop(6/33=2) iop(6/42=6) iop(6/43=20)\n')
		f.write('#IOP(5/87=12)\n')
		f.write('#density=current\n')
		f.write('\n')
		f.write('ESP det {} | {}/{}\n'.format(mol,method,bs))
		f.write('\n')
		f.write('{} {}\n'.format(charge,spin))
		for i in range(len(xyz['elem'])):
			f.write('{} {:10.5f} {:10.5f} {:10.5f}\n'.format(xyz['elem'][i],\
									xyz['x'][i],xyz['y'][i],xyz['z'][i]))

		f.write('\n')
		f.write('@def2-tzvppd-all.gbs/N\n')
		f.write('\n')
		f.write('\n')
