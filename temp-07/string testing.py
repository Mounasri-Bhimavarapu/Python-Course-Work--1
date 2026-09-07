Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=' python life '
s.strip()
'python life'
s.rstrip()
' python life'
s.lstrip()
'python life '
s.replace('','')
' python life '
s.replace(' ','')
'pythonlife'
s='python java c++'
s.split()
['python', 'java', 'c++']
s.rsplit()
['python', 'java', 'c++']
''.join(s)
'python java c++'
'-'.join()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    '-'.join()
TypeError: str.join() takes exactly one argument (0 given)
'-'.join(s)
'p-y-t-h-o-n- -j-a-v-a- -c-+-+'
a='python, java, c++'
'-'.join(a)
'p-y-t-h-o-n-,- -j-a-v-a-,- -c-+-+'
''.join(a)
'python, java, c++'
t=['python,java,c++']
''.join(t)
'python,java,c++'
'-'.join(t)
'python,java,c++'
s=['python','java','c++']
''.join()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ''.join()
TypeError: str.join() takes exactly one argument (0 given)
>>> ''.join(s)
'pythonjavac++'
>>> s='mounasri.b'
>>> s.partition('.')
('mounasri', '.', 'b')
>>> s.startswith('m')
True
>>> s.endswith('b')
True
>>> s.endswith('a')
False
>>> 'mounasr'.islower()
True
>>> '.MOUNASRI'.isupper()
True
>>> 'assaskju'.isalpha()
True
>>> 'klgser@'.isaplpha()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    'klgser@'.isaplpha()
AttributeError: 'str' object has no attribute 'isaplpha'. Did you mean: 'isalpha'?
>>> 'hgdsrfguuiop@'.isalpha()
False
>>> '3477jjgtd'.is alnum()
SyntaxError: invalid syntax
>>> 'lkgfd23456'.isalnum()
True
>>> ''  '.isspace()
SyntaxError: unterminated string literal (detected at line 1)
>>> '  '.isspace()
True
>>> 'Hello World'.istitle()
True
>>> 'else' is identifier()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    'else' is identifier()
NameError: name 'identifier' is not defined
>>> 'else' isidentifier()
SyntaxError: invalid syntax
>>> 'else'.isidentifier
<built-in method isidentifier of str object at 0x000002697ECABCC0>
