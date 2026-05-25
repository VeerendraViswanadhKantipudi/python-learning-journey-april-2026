#reg x
#regular expressions are powerful tools(module)embedded in python which is maily used to find a pattern within a give string, or statement or files and
# we mainly used for text manipulation
'''a = "codegnan"
print(a)
'''
'''a = "codegnan\nis\tin\nvij"
print(a)'''

#rstring(raww string) just like f string
'''a = r"codegnan\nis\tin\nvij"
print(a)'''

#compile(), search(), findall(), split(), sub().
#sequence characters
'''
\\w->it matches alphanumeric
\\W->it matches non-alpha-numeric
\\d>it matches any digit
\\D->it matches non-digits
\\s->it represents white spaces
\\S->it represents non-white-spaces'''

#Example
#compile()
import re
'''a = "map maths cat cash money cup cap mug codegnan"'''
'''b = re.compile(r"m\w\w\w")
print(b)'''

#search()
'''c = b.search(a)
print(c)'''

'''c = re.search(r"m\w+",a)
print(c)'''

#findall()

'''b = re.fildall(r"m\w+",a)
print(b)'''

'''b = re.findall(r"c\w+",a)
print(b)'''
'''b = re.findall("c\w+",a)
print(b)'''

#split()

'''b = re.split("m",a)
print(b)

b = re.split("\s",a)
print(b)'''




#sub() nothing but substitution
'''a = re.sub("maths", "Science",a)
print(a)'''

#\\d

'''a = "year 2026 for 234 days and 3 months and 14 hours and 32 min and 43 sec "
b = re.findall(r"\d+",a)
print(b)'''

#error and execption handeling
# there are three types of errors
#1. syntax error, 2.Run_timeerror, 3. Logical error
#1. syntax(compile error)
#2. Run_time error(during execution )
#3. Logical error(error in logic)(inbuilt error)

#1.Syntax Error
#it was mainly consistes of indententation and semoicolon missing and unclosed bracket we can check during exection
#example
'''for i in range(10)
    print(i)'''# in the above ":" is missing

#2. Run_time error
# Run_time error mainly disaplayed in the interpeter
'''a = int(input())
b = int(input())
print(a//b)'''#10//10-> zero division error

#Logial error
#this type of error will not be visible
#example
'''a = 4
b = 4
if a<b:
    print("true")'''# means we cannot be see the output
#Exception Handling
#There are four blocks iin exception handling
#1.Try
#Instructions from which we are expeting the exceptions
#2.Execpt
# exceptions is raised in try block it will be handle by this block
#3. Else
#optional(no-exceptions)
#4. Finally
#always
#Exception Handling
while True:
    a = int(input("a value "))
    b = int(input("b value "))
    try:
        c = a//b
        print(c)
    except:
        print("Exception is raised")
    else:
        print("optional")
    finally:
        print("Program ends")







