# operators overloading

'''class A():
    def __init__(self,a):
        self.a = a
    def  __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self, b):
        self.b = b
x = A(5)#x  = 5
y = B(4)#y = 4
print(x+y)'''

#method overloading

'''class New():
    def sum(self,a= None,b= None ,c = None):
        if a !=None and b!= None and c!= None:
            print("the sum is ", a+b+c)
        elif a !=None and b!= None :
            print(" the product is ", a*b)
        elif c!=None and b!= None :
            print("the product is ", c*b)
        else:
            print("program ends")
a=New()
a.sum()
a.sum(map(int, input().split()))
a.sum(map(int, input().split()))'''

'''class New():
    def sum(self,a= None,b= None ,c = None):
        if a !=None and b!= None and c!= None:
            print("the sum is ", a+b+c)
        elif a !=None and b!= None :
            print(" the product is ", a*b)
        elif c!=None and b!= None :
            print("the product is ", c*b)
        else:
            print("program ends")
a=New()
a.sum()
a.sum(3,4,5)
a.sum(6,4)'''

'''class New():
    def sum(self,a= 2,b= 3 ,c = 4):
        if a ==2  and b== 10 and c == 4:
            print("the sum is ", a+b+c)
        elif a !=None and b!= None:
            print(" the product is ", a*b)
        elif c!=None and b!=None :
            print("the product is ", c*b)
        else:
            print("program ends")
a=New()
a.sum()'''

#method overriding

'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog can bark")
a= Animal()
b= Dog()
a.speak()
b.speak()'''

'''class Vehical():
    def sound(self):
        print("Vehical can make sounds")
class Bike():
    def  sound(self):
        print("bike can but don't ask me about the sound")
class Car():
    def sound(self):
        print("cars can go faster but don't ask me about the sound it make ")
a= Vehical()
b= Bike()
c= Car()
a.sound()
b.sound()
c.sound()'''












