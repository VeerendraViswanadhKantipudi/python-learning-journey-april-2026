Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # arthematic
>>> a= 2
>>> b= 3
>>> print(a+b)
5
>>> print( a-b )
-1
>>> print (a*b)
6
>>> print(a//b)
0
>>> print(a/b)
0.6666666666666666
>>> print(a**b)
8
>>> print(a%b)
2
>>> #Assignment Operators
>>> a= 4
>>> b= 5
>>> a+=b
>>> a
9
>>> a-= 2
>>> a
7
>>> a*= 4
]
>>> a
28
>>> a/= 3
>>> a
9.333333333333334
>>> a//= 4
>>> a
2.0
>>> a**= 4
>>> a
16.0
>>> a%= 3
>>> a
1.0
>>> b+=a
>>> b
6.0
b-=a
b
5.0
b*=a
b
5.0
b**=a
b
5.0
b/=a
b
5.0
b//=a
b
5.0
b%=a
b
0.0
#Comparison(Relational)Operators
a= 2
b=22
a==b
False
a!=b
True
a>b
False
a<b
True
a>=b
False
a<=b
True
#Logical Operators
a = 32
b = 21
a and b
21
a and: b
SyntaxError: invalid syntax
a not b
SyntaxError: invalid syntax
a< 10 and b >10
False
a< 10 or b> 20
True
not (b< 10)
True
# Identity operators
a = [22, 32]
b = a
a is b
True
b is not a
False
a= [1,2,3,4]
b = a,b
a is b
False
b is a
False
b is not a
True
a is not b
True
# Membership operators
a = [22, 32, M ]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a = [22, 32, M ]
NameError: name 'M' is not defined
a = [ 21, 22, 23, 24]
23 in a
True
21 not ina
SyntaxError: invalid syntax
21 not in a
False
32 is not in a
SyntaxError: invalid syntax
32 not in a
True
# identity
a = 3
if type(a) is int
SyntaxError: expected ':'
if type (a0 id int:
         
SyntaxError: invalid syntax. Perhaps you forgot a comma?
if type (a) is int:
         print("true")

         
true

if type (a) is not int
         
SyntaxError: expected ':'
if type (a) is not int:
         print("its not int")

         

a= 5
         
if type(a) is float:
         print("True")

         
a=5.0
         
a = 5.0
         
if type (a) is float:
         print ("true")

         
true
a = "Hello World:
         
SyntaxError: unterminated string literal (detected at line 1)
a = " Hello World"
         
if type (a) is str:
         print("true")

         
true
# memembeship
         
a= 3,4,4,4,4,4
         
if 10 in a :
         print(10)

         
if 10 not in a:
         print( "not there")

         
not there
#bitwise operator
         
a= 3
         
b = 3
         
bin(a)
         
'0b11'
bin(b)
         
'0b11'
a&b
         
3
a|b
         
3
a^b
         
0
a~b
         
SyntaxError: invalid syntax
~a
         
-4
~b
         
-4
a<<b
         
24
b>>a
         
0
a>>b
         
0
b<<a
         
24
