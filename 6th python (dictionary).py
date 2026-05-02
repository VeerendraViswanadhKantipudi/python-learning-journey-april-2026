Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# dict{}
a= {"year":2026,"month":5}
print(a)
{'year': 2026, 'month': 5}
type(a)
<class 'dict'>
b={"year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['year', 'month'])
a.values()
dict_values([2026, 5])
a.items()
dict_items([('year', 2026), ('month', 5)])
a.fromkeys()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.fromkeys()
TypeError: fromkeys expected at least 1 argument, got 0
a.update({"mobileno":9392644482256561})
a
{'year': 2026, 'month': 5, 'mobileno': 9392644482256561}
a.update({"name":Veerendra},{"sec":2})
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.update({"name":Veerendra},{"sec":2})
NameError: name 'Veerendra' is not defined
a.update({"name":Veerendra,"sec":2})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.update({"name":Veerendra,"sec":2})
NameError: name 'Veerendra' is not defined
a.update({"name":"Veerendra"},{"sec":2})
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.update({"name":"Veerendra"},{"sec":2})
TypeError: update expected at most 1 argument, got 2
a.update({"name":"Veerendra","sec":2})
a
{'year': 2026, 'month': 5, 'mobileno': 9392644482256561, 'name': 'Veerendra', 'sec': 2}
#setdefault
a={"year":2026,'month':'may','date':2}
a.setdefault('date':2)
SyntaxError: invalid syntax
a.setdefault('date',2)
2
a.pop('date',2)
2

a
{'year': 2026, 'month': 'may'}
>>> a.popitem()
('month', 'may')
>>> a
{'year': 2026}
>>> a={"time":1,"min":3,"sec":4}
>>> a.copy()
{'time': 1, 'min': 3, 'sec': 4}
>>> a["time"]#accessing method
1
>>> a.get("min")#get method
3
>>> b=a
>>> b
{'time': 1, 'min': 3, 'sec': 4}
>>> a= {"year":2026,"month":5}
>>> b={'time': 1, 'min': 3, 'sec': 4}
>>> print(a)
{'year': 2026, 'month': 5}
>>> peint(a+b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    peint(a+b)
NameError: name 'peint' is not defined. Did you mean: 'print'?
\
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(a+b)
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> a.add(b)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.add(b)
AttributeError: 'dict' object has no attribute 'add'
>>> #one key with number of values
>>> details ={"idnos":[10,20,30],"names":["vara","ravali","appu"],"marks":[70,40,80]}
>>> type(details)
<class 'dict'>
>>> details.keys
<built-in method keys of dict object at 0x00000236420A56C0>
>>> details.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['vara', 'ravali', 'appu']), ('marks', [70, 40, 80])])
