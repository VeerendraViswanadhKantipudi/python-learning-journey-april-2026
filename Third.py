Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Indexing
a="Vijayawada"
a[4]
'y'
a[3]
'a'
a[0]
'V'
a[0]
'V'
a[0]+a[2]+a[3]+[4]+a[5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[0]+a[2]+a[3]+[4]+a[5]
TypeError: can only concatenate str (not "list") to str
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'Vijaya'
a= "I love Python"
a[1]
' '
a[0]
'I'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
'I love '
a=" Vijayadwada is a Royal City"
a[3]
'j'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
' Vijaya'
a[-2]
't'
a[-1]+a[-2]+a[-3]+a[-4]+a[-5]
'ytiC '
a[12]
' '
a[12]+a[13]+a[14]
' is'
a[21]
'a'
a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]
'Vijayadwada'
a= "Vizag isd a city of destiny"
a[2]
'z'
a[-8]
' '
a[2]+a[4]+a[-5]+a[-6]+a[7]+a[8]
'zgsesd'
b= "codegnan IT Solutions"
b[-1]+a[2]
'sz'
a[0]+b[0]
'Vc'
a[1]+a[2]+a[3]+a[4]+a[5]+b[1]+b[2]+b[3]+b[4]+b[5]
'izag odegn'
a[-2]+a[2]+a[3]+a[-3]+a[4]+a[-4]+a[5]+a[-5]+b[1]+b[-1]+b[2]+b[-2]+b[3]+b[-3]+b[4]+b[-4]+b[5]+b[-5]
'nzaigt sosdneogint'
b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]+b[9]+b[10]+b[11]+b[12]
'codegnan IT S'
#Slicing
a= codegnan
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a= codegnan
NameError: name 'codegnan' is not defined
a= "codegnan"
a[0:2]
'co'
a[:7]
'codegna'
a[0:8]
'codegnan'
a= "succeed"
a[:4]
'succ'
a[0:7]
'succeed'
b= "until"
b[0:5]
'until'
c="hard'
SyntaxError: unterminated string literal (detected at line 1)
c="hard"
c[0:4]
'hard'
d= "work"
d[0:4]
'work'
E= "you"
E[:2]
'yo'
E[:3]
'you'
f= " I am learning python course"
f[:27]
' I am learning python cours'
f[:28]
' I am learning python course'
a = "simple is better than complex
SyntaxError: unterminated string literal (detected at line 1)
"simple is better then complex"
'simple is better then complex'
a= "simple is better then complex"
a[-1:-7]
''
a[:-7]
'simple is better then '
a[-7:]
'complex'
a[-19:13]
'bet'
a[-19:-13]
'better'
#striding
a= "data Science"
a[::1]
'data Science'
a[::3]
'dacn'
>>> a= "c;oud Computing"
>>> a[::5]
'c u'
>>> a[:6]
'c;oud '
>>> a[8:]
'mputing'
>>> a[3:11]
'ud Compu'
>>> a[::2]
'codCmuig'
>>> a[::1]
'c;oud Computing'
>>> a[5:12]
' Comput'
>>> a= " Machine Learning"
>>> a[1:8:2]
'Mcie'
>>> a[2:11:3]
'ai '
>>> a[3:15:4]
'cea'
>>> a[1:10:5]
'Mn'
>>> a=
SyntaxError: invalid syntax
>>> a= "python Course"
>>> a= [-2:-12:14]
SyntaxError: invalid syntax
>>> a=[-2:-12;-4]
SyntaxError: invalid syntax
>>> a[-2:-12:-4]
'sCh'
>>> a[-4:-13:-6]
'uh'
>>> a[-3:-9:-6]
'r'
>>> a[-3:-9:-2]
'ro '
>>> a= "Python Course"
>>> a[7:4:2]
''
>>> a=[-9:-5:-2]
SyntaxError: invalid syntax
>>> a[-9:-5:-2]
''
