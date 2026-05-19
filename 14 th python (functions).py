#functions.
#a function is a block of orginized,resuable code and that is used to perform a single or multiple tasks.
# python gives in built function like print() you can make your own function also and these are called user defined functions.
#python block begin with the keyword def followed by the function name()"parenthesis".
'''def calculate(a,b):
    print("the sum is " ,a+b)
    print("the diff is ",a-b)
    print("the product is ",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the power is " ,a**b)
    print("the modulus is ",a%b)
    print("the product is ",a//b)
calculate(10,20)
calculate(100,200)
calculate(10,200)'''
#function in runtime.

'''def add():
    a = int(input("a value"))
    b = int(input("b value"))
    print (a+b)
add()'''

# "print "just shows the human user inout in a console(intrepeter).
#"retrn" is used to terminate the function and gives back a value from the function .
#print/ return

'''def cal(a,b):
    c = a+b
    d= a-b
    e = a*b
 #return c
 #return d
 #return e
    return c,d,e
print(cal(3,5))'''


'''def cal(a,b):
    c = a+b
    d = a-b
    e = a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''

#task 1
'''while True
def cal():
    c = int(input(" Enter options(1: Add, 2:Sub, 3: Mul):"))
    a = int(input("a value"))
    b = int(input("b value"))
    if c ==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    else:
        print("Invalid option")
       
cal()'''
#multiple def
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mult():
    print(a*b)
while True:
    a = int(input(" a value"))
    b = int(input("b value"))
    option = int(input("choose the option 1.add 2.sub 3.mult"))
    if option ==1:
        add()
    if option ==2:
        sub()
    if option==3:
        mult()'''
#task 2

'''while True:
    def cal():
        a = int(input(" No of Friends "))
        b = int(input("Amount"))
        c = b//a
        print(c)
    cal()'''

'''while True:
    def cal():
        a = int(input(" No of Friends "))
        b = int(input("Amount"))
        print(" Value per head {} ".format(b//a))
    cal()'''
    


    
'''while True:
    def cal():
        a = int(input(" No of Friends "))
        b = int(input("Amount"))
       
        print(f"the bill is {b//a}")
    cal()'''



    

