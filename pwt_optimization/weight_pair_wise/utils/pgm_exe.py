#!/bin/python
# -*- coding: utf-8 -*-

import os

def pyresp_gen(espdat,f1name,f2name,charge,wk,st,mtype):
	#f1name = espdat.split('_')[0]+'.1st'
	os.system("pyresp_gen.py -i {} -f1 {} -f2 {} -q {} -p {} -pwt1 {} -pwt2 {}".format(espdat,f1name,f2name,charge,mtype,wk,st))

def polresp_exe(f1name,f2name,espdat,stage):
	#os.system('pol_resp -O -i {0}.{1:7.6f}.1st -o {0}.{1:7.6f}.1st.out -e {2} -ip $HOME_RESP/pGM-pol-2016-09-01.dat -s {0}.{1:7.6f}.1st.esp -t {0}.{1:7.6f}.1st.chg'.format(mol,ctr,espdat))
	if stage==1:
		os.system('pol_resp -O -i {0} -o {0}.out -e {1} -ip $HOME_RESP/pGM-pol-2016-09-01 -s {0}.esp -t {0}.chg'.format(f1name,espdat))
	elif stage==2:
		os.system('pol_resp -O -i {2} -o {2}.out -e {1} -ip $HOME_RESP/pGM-pol-2016-09-01 -s {2}.esp -t {2}.chg -q {0}.chg'.format(f1name,espdat,f2name))

def pyresp_exe(f1name,f2name,espdat,stage):
	#os.system('pol_resp -O -i {0}.{1:7.6f}.1st -o {0}.{1:7.6f}.1st.out -e {2} -ip $HOME_RESP/pGM-pol-2016-09-01.dat -s {0}.{1:7.6f}.1st.esp -t {0}.{1:7.6f}.1st.chg'.format(mol,ctr,espdat))
	if stage==1:
		os.system('py_resp.py -O -i {0} -o {0}.out -e {1} -ip $HOME_RESP/pGM-pol-2016-09-01 -s {0}.esp -t {0}.chg'.format(f1name,espdat))
	elif stage==2:
		os.system('py_resp.py -O -i {2} -o {2}.out -e {1} -ip $HOME_RESP/pGM-pol-2016-09-01 -s {2}.esp -t {2}.chg -q {0}.chg'.format(f1name,espdat,f2name))


if __name__ == '__main__':
	espdat = "CH2O_ccsd_a4z_esp.dat"
	f1name = 'CH2O.0.00005.1st'
	pyresp_gen(espdat,f1name,10**-5,0)
	polresp_exe('CH2O',0.00005,espdat)
