'''variable lenth arguments are automatiacally stores in tuples and we use star arguments '''
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6)
b=[5,6,7,8,9,10]
check(*b)
c={8,9,10,2,3,4}
check(*c)
d={"name":"veerendra","city":"hanuman junction"}
check(*d)'''

'''def check(*a):
    b=2 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            b=b+i
            print(b)
check()
check(1,2,3,4,5,6)
Qcheck(1,2,3,5,5.4,5,2,2.4)
check(2,3,5,7,2.4,5.3,"Veerendra")'''

#kwargs(**)
'''def Details(**a):
    print(a)
    print(type(a))
Details()
d={"idnos":[10,20,30],
   "names":["veerendra","queen","neha"],
   "status":["P","A","P"]}
Details(**d)'''

'''def details(**a):#for dictionary we have to use double **
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])#for finding the index of i in the values
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"idnos":[10,20,30],
   "names":["Veerendra","queen","neha"],
   "status":["P","A","P"]}
details(**d)'''

#both* and **usage
'''def final (*a,**b):
    d=1
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d= d+i
            print(d)
    for i,j in b.items():
        print("key is ",i)
        print("value is",j)
final()
data = (2,3,4,5,5,4.3,"pyhton",7+9j,True,False)
final(*data)
details={"idnos":[10,20,30],
   "names":["Veerendra","queen","neha"],
   "status":["P","A","P"]}
final(**details)
final(*data,**details)'''


