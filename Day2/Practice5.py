import pprint  # if data is complex and nested, pprint helps in better readability


emp = {}

emp['eid'] = [101,102,103,104]
emp['ename'] = ['john','ram','raju','bibu']
emp['edept'] = ['sales','prod','hr','sales']
emp['dob'] = {'DOB':[{'DOB':'1st Jan'}, {'DOB':'2nd Feb'}, {'DOB':'3rd Mar'}, {'DOB':'4th Apr'}]}

# print(emp) 
pprint.pprint(emp)

