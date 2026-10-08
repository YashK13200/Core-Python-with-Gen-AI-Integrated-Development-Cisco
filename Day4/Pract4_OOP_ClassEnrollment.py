'''
We have a Class Entrollment
- Having attributes Name and DOB 
- Add 2 objects of the class
- Then Again add one more attribute 'Place' outside class  
'''
class Enrollment:
    Name = ""
    DOB = ""
    
    
    
Enrollment.Place = ""
    
obj1 = Enrollment()
obj1.Name = "Arun"
obj1.DOB = "2000-01-01"    
obj1.Place = "Chennai"


obj2 = Enrollment()
obj2.Name = "Leo"
obj2.DOB = "2001-02-02"
obj2.Place = "Bangalore"

obj3 = Enrollment()
obj3.Name = "Mia"
obj3.DOB = "2002-03-03"
obj3.Place = "Mumbai"

print(f"Name: {obj1.Name}, DOB: {obj1.DOB}, Place: {obj1.Place}")
print(f"Name: {obj2.Name}, DOB: {obj2.DOB}, Place: {obj2.Place}")
print(f"Name: {obj3.Name}, DOB: {obj3.DOB}, Place: {obj3.Place}")
