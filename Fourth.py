Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#strings
a="pthon"
len(a)
5
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#len()
#count()
#number of repeated words of the letter
#Example
count(a)# worong method
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    count(a)# worong method
NameError: name 'count' is not defined. Did you mean: 'round'?
a= "twinkle twinkle littel star"
a.count("twinkle")
2
a.count("t")
5
a.count("k")
2
a.count(" ")
3
#find a string
a="code"
a[2]
'd'
a.foind("d")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.foind("d")
AttributeError: 'str' object has no attribute 'foind'. Did you mean: 'find'?
a.find("d")
2
b= "hello"
b.find("l")
2
b[2:4]
'll'
#escape sequences
#there are two types
#1: \n->new line
#2: \t->tab space
a= "name\nmobile\tmailid"
print(a)
name
mobile	mailid
b="name:Veerendra\nmobileno:9392644482\tmailid:kantipudiveerendra@gmail.com"
print(b)
name:Veerendra
mobileno:9392644482	mailid:kantipudiveerendra@gmail.com

#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a.replace("until","then")
'wait then you succeed'
b=a.replace("wait","work")
b
'work until you succeed'
#upper
a= "code"
a.upper()
'CODE'
#lower()
b= "GNAN"
a.lower()
'code'
b.lower()
'gnan'
c= "python"
c[0].upper()
'P'
#capitlize
c.captlize()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c.captlize()
AttributeError: 'str' object has no attribute 'captlize'. Did you mean: 'capitalize'?
#capitalize()
'
c.captalize()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    c.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
c.capitalize()
'Python'
d="python course"
d.capitatlize()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d.capitatlize()
AttributeError: 'str' object has no attribute 'capitatlize'. Did you mean: 'capitalize'?
d.capitalize
<built-in method capitalize of str object at 0x00000203784E1930>
d.capitalize()
'Python course'
#title
d.title()
'Python Course'
#isupper
a="data"
a.isupper()
False
#islower
a.islower()
True
#isalpha()
a.isalpha()
True
#isdigit()
a.isdigit()
False
b="python corse"
b.isupper()
False
b.isaplha()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    b.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
b.isalpha()
False
c=12345
c.isnumeric()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    c.isnumeric()
AttributeError: 'int' object has no attribute 'isnumeric'
c="13344"
c.isnumeric()
True
c.isdigit()
True
c.isalnum
<built-in method isalnum of str object at 0x00000203784CA460>
c.alnum
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    c.alnum
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
c.alnum()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    c.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
c.isalnum()
True
a="6/2"
a.isdigit()
False
a="7.8"
a.isdecimal()
False
b=9.0
b.isdecimal()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    b.isdecimal()
AttributeError: 'float' object has no attribute 'isdecimal'
b="9"
b.isdecimal()
True
float(b)
9.0
a="Veerendra"
b="kantipudi"
print(a+b)
Veerendrakantipudi
print(a+" "+b)
Veerendra kantipudi
print(a.title()+" "+b.title())
Veerendra Kantipudi
print((a+" "+b).title())
Veerendra Kantipudi
print((a+" "+b).capitalize())
Veerendra kantipudi
#strip()
#there are thwo types of strips
#lstrip(), rstrip()
a= "       Veerendra"
a.strip()
'Veerendra'
b="     Veerendra    "
b.strip()
'Veerendra'
>>> b.lstrip()
'Veerendra    '
>>> b.rstrip()
'     Veerendra'
>>> #split()
>>> a="python c c++ java"
>>> a.split()
['python', 'c', 'c++', 'java']
>>> b="i am Learning python Full stack"
>>> b.split()
['i', 'am', 'Learning', 'python', 'Full', 'stack']
>>> c="I  am Veereendra Viswanadh Kantipudi"
>>> c.split()
['I', 'am', 'Veereendra', 'Viswanadh', 'Kantipudi']
>>> D="python,java,Css"
>>> D.split()
['python,java,Css']
>>> #join()
>>> a="aplee"," ","bannana"
>>> "".join(a)
'aplee bannana'
>>> #formatting
>>> a= 5
>>> b= 6
>>> print(a+b)
11
>>> print("the sum is",a+b)
the sum is 11
>>> print("the sum is a+b")
the sum is a+b
>>> city = "vij"
>>> print("the City is",city)
the City is vij
>>> #format Method
>>> a= "motu"
>>> b= "patlu"
>>> print("hello  {}{}".format(a,b))
hello  motupatlu
>>> print("hello  {} {}".format(a,b))
hello  motu patlu
>>> print("hello  {} hello {}".format(a,b))
hello  motu hello patlu
