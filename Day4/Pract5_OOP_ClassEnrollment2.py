class Enrollment:
    Name = ""
    DOB = ""
    place = ""
    def initialize(self,n,d,p):
        self.Name = n
        self.DOB = d
        self.place = p
        print(f"Emp Name: {self.Name}, DOB: {self.DOB}, Place: {self.place}")
        
    def display(self):
        print(f"About {self.Name}, Details:-")
        print(f"Name: {self.Name}, DOB: {self.DOB}, Place: {self.place}")
        
        
obj1 = Enrollment()
obj1.initialize("Arun", "2000-01-01", "Chennai")
obj1.display()

obj2 = Enrollment()
obj2.initialize("Leo", "2001-02-02", "Bangalore")
obj2.display()


