# Single inheriteance
'''class RBI():
    cash = 100000
    def Avaliable_cash(s):
        print("Avaiable Cash", s.cash)
        print("Avaliabe Cash", RBI.cash)
class SBI(RBI):
    cash = 25000
    def old_cash(s):
        print("old cash", s.cash)
class HDFC(RBI):
    cash = 50000
    def new_cash(s):
        print("New Cash is ",s.cash)
        print("New Cash is ",s.cash+RBI.cash)
a= HDFC()
a.Avaliable_cash()
a.new_cash()'''

#multiple Inheriteance
'''class Father():
    heigth = 6
    def Given_Height(cls):
        print("Given Height",cls.heigth)
class Mother():
    weight = 56
    def Given_Weight(cls):
        print("Given Weight is ",cls.weight)
class Child(Father,Mother):
    date_of_birth = 20-2-2024
    def Given_DOB(cls):
        print("parents height and weight",cls.heigth+cls.weight)
        print("given date of Birth",cls.date_of_birth)
a= Child()
a.Given_Height()
a.Given_Weight()
a.Given_DOB()'''

#Multi Level Inheriteance
'''class GrandFather():
    land = "5 acres"
    def Given_land(s):
        print("Grand Father have ",s.land)
class Father(GrandFather):
    house = "1000 squar feet"
    def Given_house(s):
        print("Father have ",s.house)
class GrandChild(Father):
    vehicle = "car"
    def given_vehicle(s):
        print("GrandFather and Father have" , s.land,s.house)
        print("Grand Have",s.vehicle)
a= GrandChild()
a.Given_land()
a.Given_house()
a.given_vehicle()'''

# Hybrid Inheriteance
#   Hybrid Inheriteance means combning one or more than one type inheritance for ex heriracial and multiple 
#heirachical Inheritance
#means where one parent calss is inherited my multipe child classes

#heirachical Inheritance
'''class Employee():
    def parent(s):
        print("Employee is the parent class")
class Trainer(Employee):
    def chid1(s):
        print("Trainer is the child calss")
class Developer(Employee):
    def child2(s):
        print("Developer is the chid class")
a= Trainer()
a.parent()
b= Developer()
b.parent()'''

#Hybrid Inheriteance
'''class Employee():
    def colleague(s):
        print("Employee is the one of the Employees")
class Trainer(Employee):
    def partner(s):
        print("Trainer is also one of the Employees")
class Trainee(Employee):
    def staff(s):
        print("Trainee is the assistant to the developer")
class Developer(Trainee,Trainer):
    def developemen(s):
        print("All the employee, Trainer, Developer")
class Trainee(Developer):
    def staff(s):
        print("Trainee is the assistant to the developer")
a= Trainee()
a.developemen()'''

