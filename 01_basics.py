Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#variables
a= 2
b= 4
print(a+b)
6
print
<built-in function print>
(
print(7+9)
16
a= 5
print(a)
5
x= 10
print(x)
10
z= 20
print(z)
20
print(Z)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined. Did you mean: 'z'?
y= 30
print(Y)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(Y)
NameError: name 'Y' is not defined. Did you mean: 'y'?
print(y)
30
3=6\
SyntaxError: unexpected character after line continuation character
a123456789 = 100
print(a123456789)
100
4a = 50
SyntaxError: invalid decimal literal
a4 = 50
print(a4)
50
name = "Veerendra Viswanadh"
print("name")
name
print(name)
Veerendra Viswanadh
@ = 7
SyntaxError: invalid syntax
_a = 100
print(_a1)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(_a1)
NameError: name '_a1' is not defined. Did you mean: '_a'?
print(_a)
100
_=9
print(_)
9
if = 80
SyntaxError: invalid syntax
>>> ifi = 80
>>> print(ifi)
80
>>> a= 5, b= 6
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a= 4;b=6
>>> print(a+b)
10
>>> firnt name = "Veerendra Viswanadh"\
SyntaxError: invalid syntax
>>> first_name = "Veerendra Viswanadh"
>>> print(first_name)
Veerendra Viswanadh
>>> fname = "Veerendra"
>>> lname = "kantipudi"
>>> print(fname + lname )
Veerendrakantipudi
>>> print(fname+"
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print(fname + ""+ lname)
...       
Veerendrakantipudi
>>> print(fname+" "-+ lname)
...       
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(fname+" "-+ lname)
TypeError: bad operand type for unary +: 'str'
>>> a= 9
...       
>>> print(a)
...       
9
>>> del a
...       
>>> print(a)
...       
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a4'?
>>> print(fname+" " +lname)
...       
Veerendra kantipudi
