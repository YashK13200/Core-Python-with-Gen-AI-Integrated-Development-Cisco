import sqlite3

try:
    conn = sqlite3.connect("banking.db")
except Exception as eobj:
    print(f"DB connection faield."+str(eobj))
    
    
sth = conn.cursor()
sth.execute("select *from banking")
for var in sth:
    print(var)   
conn.close()



    
