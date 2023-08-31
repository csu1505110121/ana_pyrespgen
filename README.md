# ana\_pyrespgen
This repository contains homemade scripts utilized for project pyresp_gen,doi:https://doi.org/10.1021/acs.jctc.3c00659 

+ gjf\_gen: given a dozen of `pdb` and gaussian `log` file and convert them into gjf file, you can specify methods and basis set you want in script `utils/dump_opt`

+ 345\_cmps: scripts utilized for 3 methods, namely, `RESP`, `pGM-ind`, and `pGM-perm` comparision. `bash` scripts are all for esp generation the core scripts are stored in file `pyresp_analyze.py` and `pyresp_utilies.py`

+ espdiff: `calc_diff.py` Calculating the difference between any two paired methods or basis sets; `calc_diff_ref.py` Calculating the difference between queried method or bs and referenced ones.

+ pwt\_optimization: `pGM-perm` related optimization and determination

+ qwt\_optimization: `pGM-ind` related optimization and determination

+ strategies\_cmps: strategies determination




