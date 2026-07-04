#abstraction
#hiding unnessary from user is known(called) it as a abstraction
#abstract class
#if a class contain one or more than abstract method then the class is called abstract class
#abstract method
# if the method is declared without implimentation is called abstract method
#abstraction()
'''class parent():
    def data(self):
        pass
a = parent()
a.data()'''


'''class parent():
    def data(self):
        print("Python course")
a = parent()
a.data()'''

'''from abc import ABC,abstractmethod
class parent():
    @abstractmethod
    def method1(self):
        print("codegnan")
a= parent()
a.method1()'''

'''from abc import ABC,abstractmethod
class parent(ABC):
    @abstractmethod
    def method1(self):
        print("codegnan")
a= parent()
a.method1'''


'''from abc import ABC, abstractmethod
class parent(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class child(parent):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")'''

