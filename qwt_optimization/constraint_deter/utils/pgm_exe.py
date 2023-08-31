#!/bin/python
# -*- coding: utf-8 -*-

import os

def pyresp_gen(espdat,f1name,constr,charge):
	#f1name = espdat.split('_')[0]+'.1st'
	os.system("pyresp_gen.py -i {} -f1 {} -f2 '' -q {} -p ind -qwt1 {}".format(espdat,f1name,charge, constr))

def polresp_exe(mol,ctr,espdat):
	params = [mol,ctr,espdat]
	os.system('py_resp.py -O -i {0}.{1:7.6f}.1st -o {0}.{1:7.6f}.1st.out -e {2} -ip $HOME_RESP/pGM-pol-2016-09-01 -s {0}.{1:7.6f}.1st.esp -t {0}.{1:7.6f}.1st.chg'.format(mol,ctr,espdat))
	#os.system('pol_resp -O -i {0}.{1:7.6f}.1st -o {0}.{1:7.6f}.1st.out -e {2} -ip $HOME_RESP/pGM-pol-2016-09-01.dat -s {0}.{1:7.6f}.1st.esp -t {0}.{1:7.6f}.1st.chg'.format(mol,ctr,espdat))



if __name__ == '__main__':
	espdat = "CH2O_ccsd_a4z_esp.dat"
	f1name = 'CH2O.0.00005.1st'
	pyresp_gen(espdat,f1name,10**-5,0)
	polresp_exe('CH2O',0.00005,espdat)
