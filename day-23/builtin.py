# ------------SYSTEM MODULE-----------

'''import sys

print(sys.argv[-1])
print(sys.path)
print(sys.version)
print("start")
sys.exit()
print('end') '''

'''import platform

print(platform.system())
print(platform.release())
print(platform.processor())'''

# ------------------MATH MODULE------------

'''import math

print(math.e)
print(math.pi)
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(3))
print(math.sqrt(36))
print(math.gcd(12,8))
print(math.pow(2,3))'''

#---------ROUND MODULE-----------

'''print(round(12.00001))
print(round(12.3))
print(round(12.666))
print(round(12.9999))

import math
print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.666))
print(math.ceil(12.9999))

print(math.floor(12.0001))
print(math.floor(12.3))
print(math.floor(12.666))
print(math.floor(12.9999)) '''

#------------ RANDOM MODULE-----------

'''import random

print(random.seed(7))
print(random.random())
print(random.randint(100000,999999))
print(random.uniform(1,6))

l=['r' ,'p' ,'s']
print(random.choice(l))

#----------------------------------------------

lang =['python','css' ,'java' ,'javascript']
random.shuffle(lang)
print(lang) '''

# --------COLLECTIONS------------

'''s='python programming'
d={}
for i in s:
    if  i in d:
        d[i]+=1 
    else:
        d[i]=1
print(d)  '''      
#-----------------------------------------------------------
from collections import Counter,defaultdict,deque
'''
s='python programming'
res = Counter(s)
print(res) '''

#--------------------------------------------------------

'''
products =['dal','sugar','rice','milk']
res = defaultdict
for i in products:
    res[i].append(['eggs','com','rev'])
print(res)    

           

s = 'python programming'
d= defaultdict

for i in s:
    d[i]+=1
print(d) '''

#----------------------------

'''l = deque()

l.append(10)
l.append(30)
l.popleft()
l.appendleft(20)
l.append(40)
l.pop()
l.appendleft(90)
l.append(100)
print(l)'''

name = input('enter the name:')
date_birth = int(input('enter the date of birth':))
password = 





    

