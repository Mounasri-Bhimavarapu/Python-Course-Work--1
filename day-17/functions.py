'''def function name (arguments):
            #statement
            return(optional)
    functionname(parameter)        
'''



'''def gst(price):
    print('original price:',price)
    print('final price:',price+price*0.18)

gst(1000)
gst(600)
gst(800)
gst(3000)
gst(700)   '''



'''
def table(n):
    print(f'{n}-table')
    print('-------------')
    for i in range(1,11):
        print(f'{n} * {i} ={n*i}')

for i in range (1,21):
    table(i) '''



# if we use return we need to give print function outside. if it already used inside then no need to use again.

'''def is_leap(year):
    if year % 400==0 or(year % 4==0 and year % 100 !=0):
        return 'leap year'
    else:
        return 'not a leap year'

print(is_leap(2013))
print(is_leap(1900))
print(is_leap(2002))
print(is_leap(1987))
print(is_leap(2014))
print(is_leap(2012))'''



''''def  isprime(n):
    for i in range(2,n//2+1):
        if n % i==0:
            return "not a prime number"
        
    return "prime number"    
print(isprime(5))               
print(isprime(56))
print(isprime(15))
print(isprime(2)) '''

#Positional argument

'''def display(name,email,password):
    print('name:',name)
    print('email:',email)
    print('password:',password)

display('mounasri','mounasri@gmail.com','mouna@123')    
display('mounasri@gmail.com','mouna@123','mounasri')
display('mouna@123','mounasri','mounasri@gmail.com') '''

#keyword argument

'''def display(name,email,password):
    print('name:',name)
    print('email:',email)
    print('password:',password)

display(name='mounasri',email='mounasri@gmail.com',password='mouna@123')    
display(email='mounasri@gmail.com',password='mouna@123',name='mounasri')
display(password='mouna@123',name='mounasri',email='mounasri@gmail.com')'''

# Default argument

'''def display(name,email,password=None):
    print('name:',name)
    print('email:',email)
    print('password:',password)

display(name='mounasri',email='mounasri@gmail.com')    
display(email='mounasri@gmail.com',password='mouna@123',name='mounasri')
display(password='mouna@123',name='mounasri',email='mounasri@gmail.com') '''

#tuple

'''def display(*names):
    print(names)

display('mounasri')
display('mounasri','lohitha')
display('mounasri','lohitha','usha')
display('mounasri','lohitha','usha','priyanka')'''


#dictionary

def display(**names):
    print(names)

display(n1='mounasri')
display(n1='mounasri',n2='lohitha')
display(n1='mounasri',n2='lohitha',n3='usha')
display(n1='mounasri',n2='lohitha',n3='usha',n4='priyanka')


