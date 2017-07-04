## dedupe
1. use csvdedupe_modified.py obtained a submission result as submission1 -> precision=0.413 recall=0.3
2. seperate 3 records into two or three pairs -> obtain submission2 -> precision=0.84 recall 0.65 
<br><br>
#### *************************************************************************************************************


## Deterministic Experiments:
1. 	- strategy: query db for same f+l+dob+ssn+gender
	- txt files: f_l_dob_ssn_g.txt (total: 10950)
	- submission file: per1.csv 
	- result: precision=1 and recall=0.19
<br><br>
2.	- strategy: query db for same f+l+dob+gender
	- txt files: f_l_dob_g.txt (total: 33474) (this dataset contains all the data from stgy1)
	- submission file: per2.csv
	- result: precision=0.9997 and recall=0.58
<br><br>
3.	- strategy: query db for same f+l+dob+ssn and query db for same f+l+gender+ssn, union the two query results
	- txt files: f_l_ssn_dob.txt (total: 13960), f_l_ssn_g.txt (total: 13235), union_stgy3.txt(total: 16011)
	- submission file: sub5.csv (this dataset covers all the data from stgy1)
	- result: precision=1 and recall=0.27854
<br><br>
4.  - strategy: union the dataset(f_l_dob_g.txt) from stgy2 and the dataset(union_stgy3.txt) from stgy3
	- txt files: union_stgy4.txt(total: 38635)
	- submission: sub3.csv
	- result: precision=0.9997 and recall=0.67
<br><br>
5.  - strategy: query db for same f+l+address1 and union with dataset(union_stgy4.txt) from stgy4
	- txt files: union_stgy5.txt (total: 40281)
	- submission: sub4.csv
	- result: precision=0.997 and recall=0.71
<br><br>
6.  - strategy: query db for same f+l
	- txt files: f_l.txt (total: 740281)
	- submission: sub6.csv
	- result: precision=0.06 and recall=0.736
<br><br>
#### *************************************************************************************************************

## table of fields combination

### table (A) of combination 3

| index   | combination   | pairs   | test?(y/n)   | percision   | recall   |
|---|---|---|---|---|---|
| 1   | f+l+addr  | 12460   | n  |   |   |
| 2   | f+l+phone  |   | n  |   |   |
| 3   | l+gender+ssn  |   | n  |   |   |
| 4   | f+gender+ssn  |   | n  |   |   |
| 5   | gender+ssn+dob |   | n  |   |   |
| 6   | addr+phone+dob  |   | n  |   |   |
| 7   | l+gender(M)+dob  |   | n  |   |   |
| 8   | f+gender(F)+dob  |   | n  |   |   |

### table (B) of combination 4 or 5

| index   | combination   | pairs   | test?(y/n)   | percision   | recall   |
|---|---|---|---|---|---|
| 1  | f+l+dob+ssn+gender  | 10950  | y | 1  | 0.19  |
| 2  | f+l+dob+ssn  | 13960  | n  |   |   |
| 3  | f+l+gender+ssn  | 13235  | n |   |   |
| 4  | f+l+dob+gender  | 33474  | y | 0.997  | 0.58  |
| 5  | f+l+address+phone  |   | n |   |   |
| 6  | f+l+dob+phone  |   | n |   |   |
| 7  | f+l+dob+address  |   | n |   |   |
| 8  | f+dob+gender(F)+ssn  | 2882  | n |   |   |
| 9  | f+l+ssn+addr  |  | n |   |   |
| 10 | l+gender(M)+dob+ssn  |  | n |   |   |
| 11 | f+l+dob+addr+phone  |  | n |   |   |

##please make selection for the next stage work:

### To Do Query List:
- [ ] Table A 2
- [ ] Table A 3
- [ ] Table A 4
- [ ] Table A 5
- [ ] Table A 6
- [ ] Table A 7
- [ ] Table A 8
- [ ] Table B 6
- [ ] Table B 7
- [ ] Table B 9

### To Do submit List:
- [ ] Table A 1
- [ ] Table A 2
- [ ] Table A 3
- [ ] Table A 4
- [ ] Table A 5
- [ ] Table A 6
- [ ] Table A 7
- [ ] Table A 8
- [ ] Table B 2
- [ ] Table B 3
- [ ] Table B 5
- [ ] Table B 6
- [ ] Table B 7
- [ ] Table B 8
- [ ] Table B 9