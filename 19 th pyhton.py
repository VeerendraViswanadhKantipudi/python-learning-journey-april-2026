#write a function to calculate 2*x+5 where x= 5
'''def f(x):
    print(2*x+5)
f(5)

def f():
    x = int(input("enter the value"))
    print(2*x+5)
f()'''


#annoymous functions are (nameless functions) we use a keyword called as lambda to creat annoymous
#syntax
#a= lambda arg:exp
'''a= lambda x:2*x+5
print(a(5))

a= int(input("enter the value"))
b = lambda x:2*x+5
print(b(a))'''
'''a = "codegnan"
b = lambda b:a.upper()
print(b(a))


a = "Python course"
b = lambda b:a.capitalize()
print(b(a))'''

'''a = input(" f name")
b = input("l name")
c = lambda c:(a+b)
print(c(a))'''

'''a,b = [x for x in input("enter the name ").split(",")]
c = lambda a,b:(a+" "+b).title()
print(c(a,b))
'''
# filter

'''a= [1,2,3,4,5,6,7,8,9,10]
b= list(filter(lambda a:a%2==0, a))
print(b)'''

'''a= [1,2,3,4,5,6,7,8,9,10]
if a%2==0:
    print(a)'''#Error

# if we want to clear the empty data in a list we have to use the None keyword
'''a =  [[], (),set(),{},"", None, 2,2+5j,True, False,"veerendra"]
b = list(filter(None, a))
print(b)'''

#map()-> each object from a collection and forms a new collection

'''a = [1,2,3,4,5,6,7,8,9]
b = [5,6,7,8,9,10,11,12,13]
c= list(map(max,a,b))
d= list(map(min,a,b))
e= list(map(min,c,d))
print(e)
print(d)
print(c)'''

'''a = input("data1")
b =input("data2")
print(a+b)'''

'''a,b = [x for x in input("enter the names").split(",")]
print(a+b)'''

'''a= list(map(int,input("enter the value = ").split(",")))
print(a)'''

'''a= tuple(map(int,input("enter the value = ").split(",")))
print(a)'''

'''a= list(map(str,input("enter the value = ").split(",")))
print(a)'''
'''a= list(map(eval,input("enter the value = ").split(",")))
print(a)'''

data = dict(zip(input("Keys: ").split(),map(int, input("Values: ").split())))

print(data)
