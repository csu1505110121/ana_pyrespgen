#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import argparse as ap
from pyresp_utilies import ESPDIFF,read_esp_pyresp,ESP_rmsd

def main_run(espdat,methods):
	if methods == 'diff':
		esp_qm,esp_cal = read_esp_pyresp(espdat)
		#print(esp_qm)
		#print(esp_cal)
		esp_d = ESPDIFF(esp_cal, esp_qm)
		if isinstance(esp_d, str):
			print('{:15s}: {:8s}'.format(espdat,esp_d))
		else:
			print('{:15s}: {:8.5f}'.format(espdat,esp_d))
	elif methods == 'rmsd':
		esp_qm,esp_cal = read_esp_pyresp(espdat)
		rms, rrms = ESP_rmsd(esp_cal, esp_qm)
		if isinstance(rms, str) and isinstance(rrms, str):
			print('{:15s}: RMS:{:8s} RRMS:{:8s}'.format(espdat,rms, rrms))
		else:
			print('{:15s}: RMS:{:8.5f} RRMS:{:8.5f}'.format(espdat,rms, rrms))


parser = ap.ArgumentParser(description='Utilies for PyRESP, such as calculate the Difference between QM and fitted ones\n \
										Convert Fitted charges and dipoles into prmtop file and so on')
parser.add_argument('--espdat','-i',help='Input file of esp data',required=True)
parser.add_argument('--methods','-m',help='Which method do you want to analyse: o diff| o transfer and so on',default='diff')

args = parser.parse_args()

if __name__ == '__main__':
	try:
		main_run(args.espdat,args.methods)
	except Exception as e:
		print(e)
