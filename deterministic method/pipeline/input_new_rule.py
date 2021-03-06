import sys
import os.path
import os


def input_rules(source_file, indicator):
    if not os.path.isfile(source_file):
        with open(source_file, "w") as f:
            pass

    while 1:
        os.system("cls")
        all_rules = []
        print("Current rules: ")
        with open(source_file, 'r') as f:
            for i, line in enumerate(f):
                rule = line.split("@")
                print(str(i) + ". " + rule[0])
                temp = rule[0].split("_")
                temp.sort()
                all_rules.append(temp)

        new_rule = input(
            "input the new rule(q to quit): (format as f_l_dob_gender)")
        if new_rule == 'q':
            sys.exit(0)

        ele = new_rule.split("_")

        ele.sort()

        if ele in all_rules:
            continue
    # title = ['ENTERPRISEID','LAST_','FIRST_','MIDDLE','SUFFIX_','DOB','GENDER','SSN',
    #'ADDRESS1','ADDRESS2', 'ZIP','MOTHERS_MAIDEN_NAME','MRN','CITY','STATE_','PHONE','PHONE2','EMAIL','ALIAS_']
        make_query_and_output(new_rule, ele, source_file, indicator)


def make_query_and_output(new_rule, ele, source_file, indicator):
    query_fields = []
    for each in ele:
        if each == 'f':
            query_fields.append('first_')
        elif each == 'l':
            query_fields.append('last_')
        # TODO include all the fields
        elif each == 'addr':
            query_fields.append('address1')
        elif each == 'dob':
            query_fields.append('dob')
        elif each == 'gender':
            query_fields.append('gender')
        elif each == 'ssn':
            query_fields.append('ssn')
        elif each == 'phone':
            query_fields.append('phone')
        elif each == 'email':
            query_fields.append('email')
        elif each == 'alias':
            query_fields.append('alias_')
        elif each == 'middle':
            query_fields.append('middle')
        elif each == 'zip':
            query_fields.append('zip')
        elif each == 'mrn':
            query_fields.append('mrn')

    fields_num = len(query_fields)
    where_clause = []
    for i in range(fields_num - 1):
        where_clause.append("p1.{} = p2.{} and ".format(
            query_fields[i], query_fields[i]))
    where_clause.append("p1.{} = p2.{}".format(
        query_fields[fields_num - 1], query_fields[fields_num - 1]))

    with open(source_file, 'a') as f:
        if indicator == 1:
            nr = "{}@select p1.ENTERPRISEID, p2.ENTERPRISEID from pcm p1, pcm p2 where p1.ENTERPRISEID <> p2.ENTERPRISEID and ".format(
                new_rule)
        elif indicator == 2:
            nr = "{}@select * from pcm p1, pcm p2 where p1.ENTERPRISEID <> p2.ENTERPRISEID and ".format(
                new_rule)

        for each in where_clause:
            nr = nr + each
        print(nr, file=f, end='\n')


def from_manu():
    input_source = input("select input modes: 1 for pair, 2 for detail:")
    # try:
    while 1:
        indicator = int(input_source)
        if indicator == 1:
            suffix = input("file name: ")
            input_rules("rules_pair_" + suffix + ".txt", indicator)
            break
        elif indicator == 2:
            suffix = input("file name: ")
            input_rules("rules_detail_" + suffix + ".txt", indicator)
            break
        else:
            print("input must be 1 or 2 (1 for pair, 2 for detail), input again: ")
            input_source = input()


def from_file(in_file, out_file):
    if not os.path.isfile(out_file):
        with open(out_file, "w") as f:
            pass

    with open(in_file, "r") as f1:
        for each_f1 in f1:
            fields = each_f1[:-1].split(" ")
            rule = "_".join(fields)
            make_query_and_output(rule, fields, out_file, 2)


def main():
    from_manu()
    # in_file = "rule_com.txt"
    # out_file = "rules_detail_3_field_missing.txt"
    # from_file(in_file, out_file)


if __name__ == '__main__':
    main()
