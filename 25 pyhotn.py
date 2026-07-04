# object Initilializion
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a = Details("Veerendra",22,"VJA")
print(dir(a))
a.display()'''


'''while True:
    class Details():
        #creating a constructor
        def __init__(self,name,age,place):
            self.name = name
            self.age = age
            self.place = place
        def display(self):
            print(self.name,self.age,self.place)
    a = Details(input(),int(input()),input())
    print(dir(a))
    a.display()'''

'''while True:
    class Details():
        #creating a constructor
        def __init__(self):
            self.name = input("name")
            self.age = int(input("age"))
            self.place = input("place")
        def display(self):
            print(self.name,self.age,self.place)
            a = Details("Veerendra",22,"VJA")
print(dir(a))
a.display()'''

#difference between  _ and __
#  _ = public and __  = private
#we genrally use it for private variabes that means whenever we use double leading underscore for a variable our ptython interpreter reads it as a speciall variable to avoide name conflicts with methods and inner classes
'''class  Employee():
    def __init__(self):
        self.name = "Veerendra"
        self.__salary = 10000#private variable
        self._mailid = "kantipudiveerendra69@gmail.com"
a = Employee()
print(dir(a))
print(a.name)
print(a._mailid)
 #print(a.__salary)
print(a._Employee__salary)'''
# Two Employee users
'''class Employee:
    def __init__(self, name, salary, mailid):
        self.name = name
        self.__salary = salary   # private variable
        self._mailid = mailid
# Employee 1
a = Employee("Veerendra", 10000, "veerendra@gmail.com")
# Employee 2
b = Employee("Ravi", 15000, "ravi@gmail.com")
print(a.name)
print(a._mailid)
print(a._Employee__salary)
print()
print(b.name)
print(b._mailid)
print(b._Employee__salary)'''

#polymorphism
#operator overloading
'''a = 2; b = 4
print(a+b)
print(a.__add__(b))
print(a.__add__(10))
print(a.__sub__(b))
print(a.__mul__(b))
#ptint(a.__div__(2))
print(a.__pow__(2))
print(a.__ge__(10))
print(b.__le__(20))
a= [1,2,3,4,5];b = [5,6,7,8,9]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a= "python"; b = "course"
print(a.__add__(b))
a = "code";b = "gnan"
print(a.__add__(b))
print("Veerendra".__add__("k"))
a= "Veerendra"; b= "k"
print(a.__add__(" "+b))'''


