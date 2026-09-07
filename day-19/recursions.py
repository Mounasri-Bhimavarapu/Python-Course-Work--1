'''def display(n):
    if n==11:
        return
    display(n+1)
    print(n)           # giving print after recursion gives reverse order
display(1)    '''


'''def display(s,ind):
    if ind==len(s):
        return
    display(s,ind+1)
    print(s[ind] ,end='')
display('codegnan',0)    '''


'''def display(s,ind):
    if len(s)-w+1 == ind:        # width (w)
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)

s=input('enter the string:')
w=int(input('enter the with:'))    
display(s,0,w)     '''   


''''def display(l,ind):
    if ind==len(l):
        return 0
    return l[ind] + display(l,ind+1)

l=[1,2,3,4]
print(display(l,0)) '''      


'''def display(l):
    if l==0:
        return 0
    return l % 10 + display(l//10) 

l= 43567
print(display(l))  '''    


'''def display(l):
    if l==1:
        return 1
    return l % 10 * display(l//10) 

l= 43567
print(display(l))  ''' 


'''def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))        
print(factorial(4))        
print(factorial(6))        
print(factorial(9))  '''      


#fibnocci series

'''a,b =0,1
print(a,b)
for i in range(8):
    a,b = b,a+b
    print(b) '''

'''n=int(input('enter the number:'))
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b=0,1
    print(a,b)
    for i in range(n-2):
        a,b=b,a+b
        print(b , end=" ")    '''


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(20):
    print(fib(i))            


