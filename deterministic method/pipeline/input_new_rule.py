import sys

while 1:
	all_rules = []
	print("Current rules: ")
	with open('rules_pair.txt', 'r') as f:
		for i, line in enumerate(f):
			rule = line.split("@")
			print(str(i) + ". " + rule[0])
			temp = rule[0].split("_")
			temp.sort()
			all_rules.append(temp)

	new_rule = input("input the new rule(q to quit): (format as f_l_dob_gender)")
	if new_rule == 'q':
		sys.exit(0)

	ele = new_rule.split("_")

	ele.sort()

	if ele in all_rules:
		print("this rule is already exist!")
		continue
#title = ['ENTERPRISEID','LAST_','FIRST_','MIDDLE','SUFFIX_','DOB','GENDER','SSN',
#'ADDRESS1','ADDRESS2', 'ZIP','MOTHERS_MAIDEN_NAME','MRN','CITY','STATE_','PHONE','PHONE2','EMAIL','ALIAS_']

	query_fields = []
	for each in ele:
		if each == 'f':
			query_fields.append('first_')
		elif each == 'l':
			query_fields.append('last_')
		#TODO include all the fields
		elif each == 'addr':
			query_fields.append('address1')
		elif each == 'dob':
			query_fields.append('dob')
		elif each == 'gender':
			query_fields.append('gender')
		elif each == 'ssn':
			query_fields.append('ssn')
		elif each == 'phone':
			query_fields.append('phone1')
		elif each == 'email':
			query_fields.append('email')
		elif each == 'alias':
			query_fields.append('alias_')
		elif each == 'middle':
			query_fields.append('middle')
		elif each == 'zip':
			query_fields.append('zip')

	fields_num = len(query_fields)
	where_clause = []
	for i in range(fields_num - 1):
		where_clause.append("p1.{} = p2.{} and ".format(query_fields[i], query_fields[i]))
	where_clause.append("p1.{} = p2.{}".format(query_fields[fields_num - 1], query_fields[fields_num - 1]))

	with open('rules_pair.txt', 'a') as f:
		nr = "{}@select p1.ENTERPRISEID, p2.ENTERPRISEID from pcm p1, pcm p2 where p1.ENTERPRISEID <> p2.ENTERPRISEID and ".format(new_rule)
		for each in where_clause:
			nr = nr + each
		print(nr, file=f, end='\n')
		#print(nr)
		