# age-18 and above they are eligible fro vote
'''age = int(input("age="))
if age>=18 :
    print("They are eligible fro voting")
else:
    print("they are not elogible")'''
#even and odd
'''n= int(input("number"))
if n%2==0 :
    print("even")
else:
    print("odd")'''
#leap year and not leap year
'''year= int(input())
if year%4==0:
    print("leap year")
else:
    print("not a leap year")'''
#vowels
'''vowels = ["a","e","i","o","u"]
n= input()
if n in vowels:
    print("vowels")
else:
    print("consonaunt")'''


'''name = "Veerendra"
n=input()
if n==name:
    print("welcome Veerendra")
else:
    print("Welcome Guest")'''


# multiple users
'''names=["Veerendra","nani","chowdary","bobby"]
name = input().lower()
if name in names:
    print("Welcome", name)
else:
    print("welcome user")'''
#social media user and password login
'''user = input("user name = ")
password=input("password = ")
if user =="Veerendra" :
    if password =="Nani@123":
        print("Welcome user")
else:
    print("invalid credentials")'''

'''user = input("user name = ")
password=input("password = ")
if user =="Veerendra" and password =="Nani@123"  :
    print("Welcome user")
else:
    print("invalid credentials")'''
#if-elif-else
#Bakery
'''cake_price = ["redvelvewet cake = 1200","choclate cake = 1000","almond_cake= 800","Butterscorch cake = 600","Normal cake= 400"]
Cake=input("name of the cake")
if Cake in cake_price:
    print("Cake Avaliable")
elif Cake not in cake_price:
    print("Cake Not Avaliable")
else:
    print("error")'''

'''cakee = int(input( "enter the cake price= "))
if cake==1200:
    print("redvelvet cake")
elif cake==1000:
    print("choclate cake")
elif cake==800:
    print("almond cake")
elif cake==600:
    print("butterscorch cake")
elif cake==400:
    print("normal cake")
else:
    cake("cake is not avaliable")'''
#pizza
'''pizza=int(input("enter the pizza price = ")
if pizza==1000:
    print("crispy chicken pizza")
elif pizza==800:
    print("panner prizza")
elif pizza==600:
    print("corn pizza")
elif pizza==400:
    print("normal pizza")
else:
    print("sorry pizza not avaliable")'''
#for loop
'''a=["codegnan","python","course"]'''
'''for i in a:                            # method 1
     print(i.upper(),end=",")'''
'''b=str(a)
c=b.upper()                               #method 2
print(c)'''
     
'''b=[]
for i in a:
    b.append(i.upper())                   #method 3
print(b)'''



#range task
#1
'''for i in range(0,20,2):
    print(i)'''
#2
'''for i in range(0,30,3):
    print(i)'''
#3
'''for i in range(0,50,5):
    print(i)'''
#student grade system
'''while True:
    marks = int(input("Enter the marks: "))
    if marks in range(91, 101):
        print("Grade-A")
    elif marks in range(81, 91):
        print("Grade-B")
    elif marks in range(71, 81):
        print("Grade-C")
    elif marks in range(50, 71):
        print("Grade-D")
    elif marks in range(0, 50):
        print("Fail")
    else:
        print("Invalid Input (Marks should be between 0-100)")'''

#task 1 13-05-2026
'''def backery(cake = "choclate",price = 200,qty = 1):
    print("cakes %s" %cake)
    print("price is %.2f"%price)
    print("quantity is ",qty)
backery()

def backery(cake = "strawberry",price = 2000,qty = 2):
    print("cakes %s" %cake)
    print("price is %.2f"%price)
    print("quantity is ",qty)
backery()

def backery(cake = "Rasberry",price = 2200,qty = 3):
    print("cakes %s" %cake)
    print("price is %.2f"%price)
    print("quantity is ",qty)
backery()

def backery(cake = "Veninlla",price = 500,qty = 5):
    print("cakes %s" %cake)
    print("price is %.2f"%price)
    print("quantity is ",qty)
backery()'''

# Attendance Management System
'''def attendance():
    total = int(input("Enter total number of students: "))
    present = 0
    absent = 0
    present_students = []
    absent_students = []
    for i in range(1, total + 1):
        name = input(f"\nEnter Student {i} Name: ")
        status = input(f"{name} Present or Absent (p/a): ").lower()
        if status == "p":
            present = present + 1
            present_students.append(name)
            print(f"{name} is Present")
        elif status == "a":
            absent = absent + 1
            absent_students.append(name)
            print(f"{name} is Absent")
        else:
            print("Invalid Input")
            print(f"{name} marked as Absent")]
            absent = absent + 1
            absent_students.append(name)
    print("\n========== ATTENDANCE REPORT ==========")
    print(f"\nTotal Students : {total}")
    print(f"Total Present  : {present}")
    print(f"Total Absent   : {absent}")
    print("\nPresent Students List")
    print(present_students)
    print("\nAbsent Students List")
    print(absent_students)
    percentage = (present / total) * 100
    print(f"\nAttendance Percentage : {percentage:.2f}%")
attendance()'''

'''while True:
    total = int(input("Enter total students: "))
    marks = 0
    high = 0
    low = 100
    for i in range(1, total + 1):
        m = int(input(f"Enter Student {i} Marks: "))
        marks = marks + m
        if m > high:
            high = m
        if m < low:
            low = m
    print("\n----- Marks Report -----") 
    print("Total Marks :", marks)
    print("Highest :", high)
    print("Lowest :", low)
    print("Average :", marks / total)'''
#Marks Analysis Report
'''def marks_report():
    total = int(input("Enter total students: "))
    marks = 0
    high = 0
    low = 100
    for i in range(1, total + 1):
        m = int(input(f"Enter Student {i} Marks: "))
        marks = marks + m
        if m > high:
            high = m
        if m < low:
            low = m
    print("\n----- Marks Report -----")
    print("Total Marks :", marks)
    print("Highest :", high)
    print("Lowest :", low)
    print("Average :", marks / total)
marks_report()'''

'''def report():

    total = int(input("Enter total students: "))

    marks = []

    for i in range(total):
        m = int(input("Enter marks: "))
        marks.append(m)

    print("Total :", sum(marks))
    print("Highest :", max(marks))
    print("Lowest :", min(marks))
    print("Average :", sum(marks) / total)

report()'''

'''def report():

    m = [int(input("Enter marks: ")) for i in range(int(input("Total students: ")))]

    print("Total :", sum(m))
    print("Highest :", max(m))
    print("Lowest :", min(m))
    print("Average :", sum(m)/len(m))

report()'''

#a genrator is also a function which can be used as an iterator (loop) by producing group of values, where we use yield keyword.
#yield vs return
#return will terminate the function where as yield can pass the function and go on with every successfull iteration

'''a,b= [int(x) for x in input("enter the values").split(",")]

def check(a,b):
    while a < b:
        yield a
        a= a+1
        yield b
print(*check(a,b))'''
# builtin functions in python
#print, input, len, typr, range, min, max, sum
#print()
'''print("hello World")'''
#input()
'''a = int(input())
b = int(input())
print(a+b)'''
#len()
'''a=[1,2,3,4]
print(len(a))'''
#type()
'''a= [1,2,3,4]
print(type(a))'''
#dir()
'''print(dir())'''
#range()
'''a = int(input())
for i in range(0,a,2):
    print(i)'''
#max()
'''print(max(2,3,4,5,6,7,8,9,10,12,13,14,1,5,16,17,18,19,20))'''
#min()
'''print(min(2,3,4,5,6,7,8,9,10,12,13,14,1,5,16,17,18,19,20))'''
#sum()
'''a= [1,3,4,5,7,98]
print(sum(a))'''
#list is a bultin datatype
#positional and keywords
'''def fun(name,age,marks):
    print(name, age , marks)
fun("john", 23,2234)
fun(age= 23, name="john",marks= 2232)'''

# Hotel / Restaurant Table Booking using Functions
'''def table_details():
    n = int(input("Enter number of customers: "))

    for i in range(n):
        table = int(input())
        name = input()
        items = input()
        print("Table Number:", table)
        print("Customer Name:", name)
        print("Items Ordered:", items)

table_details()'''

'''a= 3
def check1():
    print(a)
check1()
print(a)

a= 5
def final():
    global a
    print(a)
    a= 10
    print(a)
    b= 15
    b= b+a
    print(b)
final()
print(a)
print(b)'''

'''def fun(a,b):
    return print(a+b)
fun(1,3)'''


'''def main():
    name = input("your name")
    password = input("your password")
    def login(user,pwd):
        if user =="veerendra" and password =="1234":
            print("sucesses")
        else:
            print("failed")
    login(name,password)
main()'''












































