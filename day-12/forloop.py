'''types of sequence string ,list ,tuple,set,dictionary,range
for syntax: for variable in sequence.

s='python course'
for i in s:
    print(i)'''

'''l=[1,2,3,4,5]
for num in l:
    print(num)'''  

'''names=('mounasri','lohitha','usha')
for name in names:
    print(name) '''  

'''prices={23,45,567,789}
for price in prices:
    print(price)  '''  

'''ratios={1:2,2:3,3:4,4:5} 
for i in ratios:
    print(i ,ratios[i]) ''' 

 

'''for i in range(1,11):
    print(i)'''


'''for i in range(2,21,2):
    print(i)   ''' 

'''for i in range(5,101,5):
    print(i) '''  


'''for i in range(19,0,-1):
    print(i)  '''   


'''s="java program"
for i in range(len(s)):
    print(i,s[i])'''

'''s=('mounasri','lohitha','usha')
for i in range(len(s)):
    print(i,s[i])   ''' 


'''s=[1,2,3,456,567]
for i in range(len(s)):
    print(i,s[i])    '''


'''s={12,34,56,67}
for i in range(len(s)):
    print(i,s[i])'''


# enumerate:gives us sequence of given data

'''s=(1,2,34,56)
for i in enumerate(s):
    print(i)'''

'''s={1:1,2:2,3:3}
for i in enumerate(s):
    print(i,s[i[1]])    '''

'''s=[123,345,345,567]
for i in enumerate(s):
    print(i,i[0])  '''  

#jumping statements: break - to terminate the loop, continue -to skip  and continue the loop.

'''for i in range(1,11):
    if i == 5:
        continue
    print(i)'''


'''k=[1,23,45,67]
n=23
for i in k:
    if i==n:
        print(n,'found')
        
    else:
        print(n,'not found') '''

'''f=[34,56,78]
n=34
for i in f:
    if i==n:
        print(n,'found')
else:
    print(n, 'not found') '''                      


'''pin=1234
for i in range(5):
    epin=int(input('enter the pin:'))
    if epin==pin:
        print('unlock the phone')
        break
    else:
        print('invalid pin')
else:
    print('try after 30 seconds')  '''          



n= int(input('enter the number:'))
for i  in range(2,n//2+1):
    if n % 1 ==0 or n % n==0:
        print('not a prime number')
        break
else:
    print('prime number')      