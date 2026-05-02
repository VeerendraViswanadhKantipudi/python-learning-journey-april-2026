Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# list[]
a=[ 4,5.6,"python",5+9j,True,False]
print(a)
[4, 5.6, 'python', (5+9j), True, False]
type(a)
<class 'list'>
b= 8.9
type(b)
<class 'float'>
type(a)
<class 'list'>
#extend
#append
a.append("html")
a
[4, 5.6, 'python', (5+9j), True, False, 'html']
a.append("css","java")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("css","java")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["css","java"])
a
[4, 5.6, 'python', (5+9j), True, False, 'html', ['css', 'java']]
b=["apple","banna","mango"]
b
['apple', 'banna', 'mango']
b.append([1,"orange"])
b
['apple', 'banna', 'mango', [1, 'orange']]
b.append[1,"orange"]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b.append[1,"orange"]
TypeError: 'builtin_function_or_method' object is not subscriptable
#extend
a=["de","ai","ml"]
a.extend(["python","java","css"])
a
['de', 'ai', 'ml', 'python', 'java', 'css']
#insert
a=["apple","mango","orange"]
a.insert(1,"bannana")

a
['apple', 'bannana', 'mango', 'orange']
\
#methods
a=["c","c++","java","ml"]
a.index("java")
2
a.copy()
['c', 'c++', 'java', 'ml']
a
['c', 'c++', 'java', 'ml']
a.clear()
a
[]
b=[]
b.append("data")
b
['data']
#sort
a=["whoite","black","red","green"]
a.sort()
a
['black', 'green', 'red', 'whoite']
b=[2,3,54,5,6,7,7,64,7,5]
b.sort()
b
[2, 3, 5, 5, 6, 7, 7, 7, 54, 64]
c= ["!","#","@","$","%"]
c.sort()
c
['!', '#', '$', '%', '@']
# reverse
a=["hi","he","heloo"]
a.reverse()
a
['heloo', 'he', 'hi']
b.reverse()
\
b
[64, 54, 7, 7, 7, 6, 5, 5, 3, 2]
#for desnding order frst we have to use sort and then use reverse
c= [1/2,3/4,4/5]
c.sort()
c
[0.5, 0.75, 0.8]
type(c)
<class 'list'>
c.reverse()
c
[0.8, 0.75, 0.5]
# we can't use sort()and reverse() at the same time we have use them differently but we can we like this a.sort(reverse=True)
#pop
a.clear()
a
[]
a=[2,34,5,6,]
a.pop()
6
s
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s
NameError: name 's' is not defined
a
[2, 34, 5]
#we can't give the number or the data int the variable directly but we can give the position of the data in the variable
#EX
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.pop(5)
IndexError: pop index out of range
a.pop(2)
5
#in the above Example we can delete the data in the variable by giving the position
a
[2, 34]
len(a)
2
a.count("Green"0
        
SyntaxError: '(' was never closed
a.count("Green")
        
0
a.count("a")
        
0
a.count("r')
        
SyntaxError: unterminated string literal (detected at line 1)
a.count("r")
        
0
#tuple()
        
a=(1,2,3,4,5,6,7,7,8)
        
print(a)
        
(1, 2, 3, 4, 5, 6, 7, 7, 8)
type(a)
        
<class 'tuple'>
a.len(a)
        
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.len(a)
AttributeError: 'tuple' object has no attribute 'len'
len(a)
        
9
a.index(10)
        
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a.index(10)
ValueError: tuple.index(x): x not in tuple
a.index(3)
        
2
b.count(1)
        
0
a.duplicate()
        
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.duplicate()
AttributeError: 'tuple' object has no attribute 'duplicate'
>>> duplicate(a)
...         
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    duplicate(a)
NameError: name 'duplicate' is not defined
>>> a= [9,1,5,2,8,4,6,3,7,0]
...         
>>> a.sort()
...         
>>> a
...         
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.insert(0,9)
...         
>>> a
...         
[9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.pop(9)
...         
8
>>> a
...         
[9, 0, 1, 2, 3, 4, 5, 6, 7, 9]
>>> a.insert(8,8)
...         
>>> a
...         
[9, 0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
>>> a.sort()
...         
>>> a
...         
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
>>> a.clear()
...         
>>> a
...         
[]
>>> a = [9,1,5,2,8,4,6,3,7,0]
...         
