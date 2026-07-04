#kaggle
#simple mail
#Email Automation
'''import random
import math
import smtplib'''#simple mail transfer libirary protocol
'''digits = "0123456789"
OTP = ""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"Your OTP"
msg = otp

s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("kantipudiveerendra69@gmail.com","ddos ktdg squb hqaa")
user = "kantipudiveerendra69@gmail.com"
email = input("Enter the Mail which you want to send otp")
s.sendmail(user,email,msg)

while True:
    a = input("Enter the otp")
    if a==OTP:
        print("OTP is Correct")
        break
    else:
        print("wrong otp")
        break'''

# ============================================
# OOP (OBJECT-ORIENTED PROGRAMMING) NOTES
# ============================================
# CLASS: A class contains attributes (variables) and methods (functions) that can manipulate the data.
#         A class is the blueprint of an object.

# OBJECT: An object is an instantiation of a class.

# METHODS: Methods are functions defined inside the body of a class.

# ============================================
# FOUR PILLARS OF OOP
# ============================================

# 1. POLYMORPHISM (Contains 4 types):
#    1) Operator Overloading
#    2) Operator Overriding
#    3) Method Overloading
#    4) Method Overriding

# 2. ENCAPSULATION (Contains 3 types):
#    1) Public
#    2) Protected Data
#    3) Private

# 3. ABSTRACTION (Contains 2 types):
#    1) Abstract Method
#    2) Abstract Class

# 4. INHERITANCE (Contains 5 types):
#    1) Single
#    2) Multiple
#    3) Multi-level
#    4) Hybrid
#    5) Hierarchical

# ============================================
# END OF NOTES
# ============================================
# OOP NOTES: Class = blueprint with attributes & methods | Object = instance of class | Methods = functions
#inside class | FOUR PILLARS: 1) Polymorphism (Operator Overloading, Operator Overriding)/
#| 2) Encapsulation (Public, Protected, Private) | 3) Abstraction (Abstract Method, Abstract Class)
#| 4) Inheritance (Single, Multiple, Multi-level, Hybrid, Hierarchical)
#Example:
'''class classname():
    name= "Codegnan"
    year = 2018
    city = "vja"
    def fname(method_name):
        print("statements.....")
a = classname()
a.fname()'''

#class declaration
'''class Details():
    name = "Veerendra"
    age = 22
    place = "vja"
    def Display(self):
        print(self.name,self.age,self.place)
a = Details()
print(dir(a))
a.Display()'''

#object Instantiation
'''class Details():
    def Data(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name , self.age, self.place)
        
a = Details()
print(dir(a))
a.Data("Veerendra",22,"vja")
a.display()
b = Details()
b.Data("nani",22,"vja")
b.display()'''

