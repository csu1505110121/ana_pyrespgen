#!/bin/bash

pyresp=py_resp.py

SMALL=(H2O ClH NH3 NH4+ CH4 CH2O C2H2 C2H4 CH3Cl CH3F CH3OH oh2oh2)
LARGE=(C2H6 C3H4 C3H8 C3N2H4 C3NOH3 C3NOH3p C4H10 C4NH4 C4OH4 C5NH5 C6H6 CH3Br CH3COCH3 CH3NH2 CH3OCH3 CH3S2CH3 CH3SCH3 CH3SO2CH3 CHONH2 CHOOCH3 CHOOH NMA PO3CH5)


for i in ${LARGE[*]}
do
	espdata=../../../../LARGE/mp2/${i}_mp2_a5z.dat
	mkdir -p ${i}/3resp
	cat <<-EOF > ${i}/3resp/py_resp.run
		#!/bin/csh -f
		echo " "
		echo " py_resp command"
		echo " "
		echo RESP stage 1:
		${pyresp} -O \\
			-i ${i}.1st \\
			-o ${i}.1st.out \\
			-e ${espdata} \\
			-s ${i}.1st.esp \\
			-t ${i}.1st.chg       || goto error

		echo RESP stage 2:
		${pyresp} -O \\
			-i ${i}.2nd \\
			-o ${i}.2nd.out \\
			-e ${espdata} \\
			-s ${i}.2nd.esp \\
			-t ${i}.2nd.chg \\
			-q ${i}.1st.chg       || goto error

		echo No errors detected
		exit(0)
		
		error:
			echo Error: check .out and try again
		exit(1)
		EOF
	(cd ${i}/3resp; rm ${i}.*; pyresp_gen.py -p chg -i ${espdata} -f1 ${i}.1st -f2 ${i}.2nd; chmod +x py_resp.run; ./py_resp.run)

done

