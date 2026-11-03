class Harsh:
    
    def h_getdata(self):
        self.hid=input("Enter Harsh's ID:")
        self.hsub=input("Enter Harsh's Subject:")
        
        
class ashok(Harsh):
    aid:int
    asub:str
    
    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class gopal(ashok):
    gid:int
    gsub:str
    
    def g_getdata(self):
        self.gid=input("Enter Gopal's ID:")
        self.gsub=input("Enter Gopal's Subject:")


class Alphabit(gopal):
    def printdata(self):
        print("--------Harsh's Data--------")
        print("Harsh's ID:",self.hid)
        print("Harsh's Subject:",self.hsub)
        print("--------Ashok's Data--------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("--------Gopal's Data--------")
        print("Gopal's ID:",self.gid)
        print("Gopal's Subject:",self.gsub)


    
ai=Alphabit()
ai.h_getdata()
ai.a_getdata()
ai.g_getdata()
ai.printdata()
