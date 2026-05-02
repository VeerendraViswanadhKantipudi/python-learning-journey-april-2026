Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sets{}
a= {2,6.5,"python",7+9j,True,False}
print(a)
{False, True, (7+9j), 2, 'python', 6.5}
type(a)
<class 'set'>
#add(0
#add()
a={2,3,4,5,6}
a.add(10)
A
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a
{2, 3, 4, 5, 6, 10}
a={1,2,3,4,5,6}
b={4,5,6}
b.issubset(a)
True
a.issubset(b)
False
a={6,7,8,9,10,11,12}
b={9,10,11,12}
a.issuperset(b)
True
b.issuperset(a)
False

#union()
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
\
a
{1, 2, 3, 4, 5, 6, 7}
#intersection
a.intersection(b)
{5, 6, 7}
#union()
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
c={13,14,15,16}
c.updte(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c.updte(a)
AttributeError: 'set' object has no attribute 'updte'. Did you mean: 'update'?
c.update(a)
c
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16}
a.union(c)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16}
a.difference(b)
set()
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}
a.difference(b)
{1, 2, 3, 4}
b.difference(a)
{8, 9, 10, 11}
a.symmetric_differenc(b)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.symmetric_differenc(b)
AttributeError: 'set' object has no attribute 'symmetric_differenc'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(b)
{1, 2, 3, 4, 8, 9, 10, 11}
a.intersection_update(a)
a
{1, 2, 3, 4, 5, 6, 7}
#intersection_update()
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}
a.symmetric_difference_update(b)
b
{5, 6, 7, 8, 9, 10, 11}
a
{1, 2, 3, 4, 8, 9, 10, 11}
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}
a.difference_update(b)
a
{1, 2, 3, 4}
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}
a.copy()
{1, 2, 3, 4, 5, 6, 7}
a.clear()
a
set()
a={1,2,3,4,5,6,7}
b={5,6,7,8,9,10,11}
a.add()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.add()
TypeError: set.add() takes exactly one argument (0 given)
a.add(12)
a
{1, 2, 3, 4, 5, 6, 7, 12}
#pop
#in sets
>>> a={1,2,3,4,5,6,7}
>>> a.pop(0)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.pop(0)
TypeError: set.pop() takes no arguments (1 given)
>>> a.pop()
1
>>> a
{2, 3, 4, 5, 6, 7}
>>> a.remove(3)
>>> q
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> a
{2, 4, 5, 6, 7}
>>> a.discard(2)
>>> A
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
>>> a
{4, 5, 6, 7}
>>> a={1,2,3,4,5,6,7}
>>> b={5,6,7,8,9,10,11}
>>> a.isdisjoint(b)
False
>>> a.count(1)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
>>> a..index(2)
SyntaxError: invalid syntax
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
