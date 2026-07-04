#super function in inheritance
'''class parent():
    def __init__(self, name):
        self.name = name
        print("parent constructor")
class child(parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("child constructor")
a = child("Veerendra", 22)
print(a.name)
print(a.age)'''

#Encapsulation
#combine multiple units into singel unit is known as Encapsulation
#it contains publicdara , private data, protected data.
#publicdata()
'''class parent():
    publicdata = 100
    def method1(self):
        print(self.publicdata )
class child(parent):
    def method2(self):
        print(self.publicdata)
a= child()
a.method1()
a.method2()
print(a.publicdata )
print(a.publicdata )'''

#_protecteddata ()
'''class parent():
    _protecteddata=10 # for protecteddata we use single underscore 
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)

obj1=child()
obj1.method1()
obj1.method2()'''

#__privatedata()
'''class parent():
    __privatedata = "Veerendra"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
a = child()
a.method1()
a.method2()'''

        
