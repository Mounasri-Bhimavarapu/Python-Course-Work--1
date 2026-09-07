Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = input ()
'codegnan'
>>> a
"'codegnan'"
>>> a = input()
1234
>>> a
'1234'
>>> a = input('Enter your Name:')
Enter your Name:mounasri
>>> Enter Your Name
SyntaxError: invalid syntax
>>> mounasri
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mounasri
NameError: name 'mounasri' is not defined
>>> cgpa=flaot(input('enter the cgpa'))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cgpa=flaot(input('enter the cgpa'))
NameError: name 'flaot' is not defined. Did you mean: 'float'?
>>> cgpa = flaot(input('enter the cgpa'))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cgpa = flaot(input('enter the cgpa'))
NameError: name 'flaot' is not defined. Did you mean: 'float'?
>>> cgpa = float(input('enter the cgpa'))
enter the cgpa 9.4
>>> cgpa
9.4
>>> names = input('enter names')
enter names mounasri usha lohitha
>>> names
' mounasri usha lohitha'
>>> names.split(',')
[' mounasri usha lohitha']
>>> names = tuple(input('enter names'))
enter namesmounasri usha lohitha
>>> names
('m', 'o', 'u', 'n', 'a', 's', 'r', 'i', ' ', 'u', 's', 'h', 'a', ' ', 'l', 'o', 'h', 'i', 't', 'h', 'a')
>>> names. split('')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    names. split('')
AttributeError: 'tuple' object has no attribute 'split'
names = input('enter names')
enter namesmounasri usha lohitha
names
'mounasri usha lohitha'
names.split()
['mounasri', 'usha', 'lohitha']
names =tuple(input(' enter names'))
 enter namesmounasri usha lohitha 
names
('m', 'o', 'u', 'n', 'a', 's', 'r', 'i', ' ', 'u', 's', 'h', 'a', ' ', 'l', 'o', 'h', 'i', 't', 'h', 'a', ' ')
names = tuple(input('enter names').split())
enter namesmounasri usha lohitha
names
('mounasri', 'usha', 'lohitha')
('mounasri', 'usha', 'lohitha')
('mounasri', 'usha', 'lohitha')
marks=input().split()
marks = 35 49 30 40
marks
['marks', '=', '35', '49', '30', '40']
marks=list(map(int,input('enter the marks').split()))
enter the marks35 49 30 40
marks
[35, 49, 30, 40]
marks = tuple(map(int,input('enter the marks').split()))
enter the marks35 49 30 40
marks
(35, 49, 30, 40)
marks =list(map(float,input('enter marks').split()))
enter marks35 49 30 40
marks
[35.0, 49.0, 30.0, 40.0]
marks=set(map(float('enter marks').split()))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    marks=set(map(float('enter marks').split()))
ValueError: could not convert string to float: 'enter marks'
marks=set(map(float,input('enter marks').split()))
enter marks35 49 30 40
marks
{40.0, 49.0, 35.0, 30.0}
names= list(map(input('enter names').split()))
enter namesnamesmounasri usha lohitha
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    names= list(map(input('enter names').split()))
TypeError: map() must have at least two arguments.
name,marks=input('enter name ,marks').split())
SyntaxError: unmatched ')'
names,marks=input('enter name,marks').split()
enter name,marks mounasri,50
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    names,marks=input('enter name,marks').split()
ValueError: not enough values to unpack (expected 2, got 1)
names,marks=input('enter names,marks').split()
enter names,marks mounasri 30
names
'mounasri'
marks
'30'
int(marks)
30
length,breath,height=list(map(int,input().split()))
length,breath,height=list(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    length,breath,height=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'length,breath,height=list(map(int,input().split()))'
length,breath,height=list(map(int,input().split()))
20 30 40
length
20
breath
30
height
40
status=eval(input())
true
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    status=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
status = eval(input())
True
status
True
type(status)
<class 'bool'>
status=eval(input())
12+67j
status
(12+67j)
type(status)
<class 'complex'>
status=eval(input())
[1,2,3,4]
status
[1, 2, 3, 4]
type(status)
<class 'list'>
a=eval(input())
{1,2,3,4,}
a
{1, 2, 3, 4}
type(a)
<class 'set'>
