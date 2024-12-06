"""class User():
    fname = "Elisha"
    lname = "Sonaha"
    def access_to(self):
        print("this is the method of class")
u = User()   # u = instance
print(u.fname)
print(u.lname)
u.access_to()"""


# constructor
class User:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print("my name is",self.fname,"",self.lname)
    def user_info(self,address):
       self.address = address
       print("name access from method is :", self.fname,"",self.lname)
       print(f"my address is{self.address}")
u1 = User("Elisha","Sonaha")    
u1.user_info("Bardiya")


u2 = User("tillotama","municipality")