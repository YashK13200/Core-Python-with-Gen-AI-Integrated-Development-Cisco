'''
read emp.csv file - line by line
search - dept in sales and living city = "Pune"
                                         =======
                                            |=> Substitute "Pune" with "Hyderabadh"
'''

import re
fname = "C:/Users/Public/Downloads/Python (x86)/Training/Day1/Day1/Py Training/Day-1/emp.csv"

fobj = open(fname, "r")
for var in fobj:
    if re.search("sales", var,re.I):
        s = re.sub('pune','Hyderabadh',var)
        if(re.search("hyderabad", s,re.I)):
            print(s.strip())

