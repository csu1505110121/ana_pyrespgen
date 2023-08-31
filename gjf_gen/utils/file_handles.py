#!/bin/python
# -*- coding: utf-8 -*-

import os,sys
CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]
config_path = CURRENT_DIR.rsplit('/',1)[0]
sys.path.append(config_path)

import numpy as np
import pandas as pd


def read_pdb(filename:str) -> pd.DataFrame:
	pdb_info = {'ATOM':[],\
				'idx':[],\
				'ATYPE':[],\
				'RES':[],\
				'CHAIN':[],\
				'RESID':[],\
				'x':[],'y':[],'z':[],\
				'OCC':[],'BETA':[]}
	with open(filename,'r')  as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if 'ATOM' in line or 'HETATM' in line:
					pdb_info['ATOM'].append(line[0:6].strip())
					pdb_info['idx'].append(int(line[6:11].strip()))
					# special line for atom type
					atype = []
					for i in line[12:16].strip().rstrip('0123456789'):
						if i.isalpha():
							atype.append(i)
						else:
							break
					atomtype = ''.join(atype)
					pdb_info['ATYPE'].append(atomtype)
					pdb_info['RES'].append(line[17:20].strip())
					pdb_info['CHAIN'].append(line[21].strip())
					pdb_info['RESID'].append(int(line[22:26].strip()))
					pdb_info['x'].append(float(line[30:38].strip()))
					pdb_info['y'].append(float(line[38:46].strip()))
					pdb_info['z'].append(float(line[46:54].strip()))
					if len(line[54:60].strip()):
						pdb_info['OCC'].append(float(line[54:60].strip()))
					else:
						pdb_info['OCC'].append(1.0)
					if len(line[60:66].strip()):
						pdb_info['BETA'].append(float(line[60:66].strip()))
					else:
						pdb_info['BETA'].append(0.0)

	pdb_info = pd.DataFrame(pdb_info)
	return pdb_info

def dump_pdb(pdbinfo:pd.DataFrame, filename:str, conn:dict=None) -> None:
	with open(filename,'w') as f:
		for i in range(pdbinfo['ATOM'].shape[0]):
			f.write('%-6s%5d%1s%-5s%-3s%1s%1s%4d%4s%8.3f%8.3f%8.3f%6.2f%6.2f\n' \
					%(pdbinfo['ATOM'].values[i],pdbinfo['idx'].values[i],'',\
						pdbinfo['ATYPE'].values[i],pdbinfo['RES'].values[i],'',\
						pdbinfo['CHAIN'].values[i],pdbinfo['RESID'].values[i],'',\
						pdbinfo['x'].values[i],pdbinfo['y'].values[i],pdbinfo['z'].values[i],\
						pdbinfo['OCC'].values[i],pdbinfo['BETA'].values[i]))

		if conn is not None:
			for k,v in conn.items():
				f.write('{:6s} '.format('CONECT'))
				f.write('{:4d} '.format(k+1))
				for x in v:
					f.write('{:4d} '.format(x+1))
				f.write('\n')

	# also needs to add connection info here

def dump_xyz(xyz:pd.DataFrame, filename:str) -> None:
	with open(filename,'w') as f:
		f.write('{:6d}\n'.format(len(xyz['idx'])))
		f.write('xyz dump info\n')
		for x in range(len(xyz['idx'])):
			f.write('{:5d} {:10.5f} {:10.5f} {:10.5f}\n'.format(xyz['idx'][x],\
										xyz['x'][x],xyz['y'][x],xyz['z'][x]))


def make_dir(dirs:str) ->None:
	for diri in dirs:
		if not os.path.exists(diri):
			os.makedirs(diri)


def read_log(filename:str) -> pd.DataFrame:
	XYZ = {'elem':[],\
			'x':[],'y':[],'z':[]}
	with open(filename,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				if 'Charge =' in line:
					count = 0
					for i in range(99999):
						line = f.readline()
						if len(line.strip()) !=0:
							XYZ['elem'].append(line.split()[0])
							count +=1
						else:
							break
					XYZ['x'] = np.zeros(count)
					XYZ['y'] = np.zeros(count)
					XYZ['z'] = np.zeros(count)
				if 'Standard orientation:' in line:
					for x in range(4):
						line = f.readline()
					for x in range(99999):
						line = f.readline()
						if '---' not in line:
							XYZ['x'][x] = float(line.split()[3])
							XYZ['y'][x] = float(line.split()[4])
							XYZ['z'][x] = float(line.split()[5])
						else:
							break

	return XYZ




if __name__ == '__main__':
	logfile = '../OPT/LARGE/CH3S2CH3.log'
	xyz = read_log(logfile)
	print(xyz)
