#!/bin/bash

SMALL=(H2O ClH NH3 NH4+ CH4 CH2O C2H2 C2H4 CH3Cl CH3F CH3OH oh2oh2)
LARGE=(C2H6 C3H4 C3H8 C3N2H4 C3NOH3 C3NOH3p C4H10 C4NH4 C4OH4 C5NH5 C6H6 CH3Br CH3COCH3 CH3NH2 CH3OCH3 CH3S2CH3 CH3SCH3 CH3SO2CH3 CHONH2 CHOOCH3 CHOOH NMA PO3CH5)

for i in ${LARGE[*]}
do
	espdata=${i}.2nd.esp
	if [ $i != 'H2' ]; then
		(cd ${i}/3resp; pyresp_analyze.py -i ${espdata} -m rmsd) 
	fi
done
