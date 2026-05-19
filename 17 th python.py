# global variables and local variables
'''variables inside and outside the functionis caled global and local variables

a variable define above the function and its accesiable to the entier global space is called the global variable
a variable define inside the function is called local variable'''

#first case of global variable
'''a= 3
def check1():
    print("inside value is ",a)
check1()
print("outside value is",a)'''

#second case of global variable
'''a = 2
def check2():
    a= 5
    a= a**2
    print("inside value is",a)
check2()
print("outside valuen is",a)'''

#third case of both global and local variables
'''a = 4
def check3():
    a= 5
    print("inside value is",a)
    c= 10
    print("updetedvalue",a+5)
    b=12#local variable
    b= b+a
    print("value of is",b)
check3()
print("a value is",a)
print("b value is ",b)'''

#usage of global keyword
'''when user wants to accesses the global variable inside the function directly and carry forward the
updated value even outside the function then we need to use the global key word'''

'''a= 5
def final():
    global a
    print("inside value is",a)
    a= 10
    print("update value is ",a)
    #global b
    b= 15#local variable
    b= b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''


'''a= 5
def final():
    global a,b
    print("inside value is",a)
    a= 10
    print("update value is ",a)
    #global b
    b= 15#local variable
    b= b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#generators
#no tuple compheresion in above cases if we remove those braces and keep paranthesis then the outcome is generated 
# a = [exp for var in collection/range]
'''a = [i for i in range (21)]
print(a)
print(type(a))'''


'''a = [i for i in range (21)]
print(*a)
print(type(a))'''
'''a = (i for i in range (21))
print(*a)
print(type(a))'''

'''a = (i for i in range (21))
print(list(a))
print(type(a))'''

'''a = (i for i in range (21))
print(set(a))
print(type(a))'''

#generator is also a function which can be used as an iterator(loop) by producing group of values where we use yield key word
#yeild vs return
# return will terminate the fuinction where as yield can pass the function and go on with every succesesful iteration

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
    print(check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a 
        a=a+1
        #yield a 
    print(check(a,b))'''

#yeild vs return
'''def mygen():
    #return"python"
    #return"java"
    #return"DSA"
    return "python","java","DSA"
print(*mygen())'''

'''def mygen():
    yield "vja"
    yield "vzg"
    yield "hyd"
print(*mygen())'''
#next()
'''def mygen():
    yield "vja"
    yield "vzg"
    yield "hyd"
print(*mygen())
d= mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))'''

     





