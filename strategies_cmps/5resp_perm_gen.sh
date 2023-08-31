#!/bin/bash

pyresp=py_resp.py

SMALL=(CH4 CH3Cl CH3F CH3OH)
LARGE=(C2H6 C3H8 C4H10 CH3Br CH3COCH3 CH3NH2 CH3OCH3 CH3S2CH3 CH3SCH3 CH3SO2CH3 CHOOCH3 NMA PO3CH5)

for i in ${LARGE[*]}
do
	espdata=../../../../../LARGE/mp2/${i}_mp2_a5z.dat
	mkdir -p ${i}/5resp-perm
	cat <<-EOF > ${i}/5resp-perm/py_resp.run
		#!/bin/csh -f
		echo " "
		echo " py_resp command"
		echo " "

		setenv AMBERHOME /Users/zhuqiang/Documents/software/pol_resp
		echo RESP stage 1:
		${pyresp} -O \\
			-i ${i}.1st \\
			-o ${i}.1st.out \\
			-e ${espdata} \\
			-ip ${HOME_RESP}/pGM-pol-2016-09-01 \\
			-s ${i}.1st.esp \\
			-t ${i}.1st.chg       || goto error

		echo RESP stage 2:
		${pyresp} -O \\
			-i ${i}.2nd \\
			-o ${i}.2nd.out \\
			-e ${espdata} \\
			-ip ${HOME_RESP}/pGM-pol-2016-09-01 \\
			-s ${i}.2nd.esp \\
			-t ${i}.2nd.chg \\
			-q ${i}.1st.chg       || goto error

		echo No errors detected
		exit(0)
		
		error:
			echo Error: check .out and try again
		exit(1)
		EOF

	(cd ${i}; cd 5resp-perm; rm ${i}.* ; pyresp_gen.py -i ${espdata} -f1 ${i}.1st -f2 ${i}.2nd -p 'perm' -pwt2 0.0001 -strategy 1; chmod +x py_resp.run; ./py_resp.run)
	#(cd ${i}; cd 5resp-perm; rm ${i}.*; rm pyrespgen.* )
	#(cd ${i}; cd 3resp; pyresp_gen.py -i ../${espdata} -f1 ${i}.1st -f2 ${i}.2nd)

done

