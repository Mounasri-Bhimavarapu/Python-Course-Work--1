Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import keyword
print(keyword.keyword)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(keyword.keyword)
AttributeError: module 'keyword' has no attribute 'keyword'. Did you mean: 'iskeyword'?
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist))
35
>>> a=10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>>  a=10
...  
SyntaxError: unexpected indent
>>> a,b=b,a
>>> a,b=b,a
>>> a
10
>>> 
>>> b
20
>>> a=3
>>> b=4
>>> a,b=b,a
>>> a
4
>>> b
3
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a
NameError: name 'a' is not defined
