'''i=1
while i<=10:
    print(i)
    i+=1  '''



'''i=10
while i>0:
    print(i)
    i-=1  '''  



'''i=5
while i<=50:
    print(i)
    i+=5  ''' 
   

'''s='while loop'
i=0
while i < len(s):
    print(s[i])
    i+=1  '''


''''s='while loop'
i=len(s)-1
while i>= 0:
    print(s[i])
    i-=1'''




'''l=[5467,5678,6789,987]
i=0
while i < len(l):
    print(l[i])
    i+=1    '''


'''n=8765
sumofdigits=0
while n>0:
    sumofdigits += n%10
    n//=10
print('sumofdigits',sumofdigits) '''



'''n=6789
while n>0:
    print(n%10)
    n//=10 '''


'''n=123456
productofdigits=1
while n >0:
    productofdigits *= n%10
    n//=10
print('productofdigits:',productofdigits) '''


'''n=45678
res=0
while n >0:
    rem =n%10
    res = res *10 + rem
    n//=10
print(res) '''   


'''n=23456
res=0
while n > 0:
    rem = n%10
    if rem%2==0:
        res += rem
    n//=10
print(res)  '''      


'''l=[7,9,23,0,0,0,12,0,13,1,0,4,0,1,4,5,6,6,13,0]

while 0 in l:
    l.remove(0)
print(l)  '''  


'''l= [1,2,6,7,25,34,56,75,34]

i=0
j=len(l)-1
while i <= j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j]) 
        i+=1
        j-=1   '''
    
    
    
data={
    'salt':25,
    'sugar':30,
    'rice':40,
    'coconut':40,
    'dal':20,
    'wheatflour':20,
    'butter':70,
    'bread':55,
    'eggs':80
}

for i in data:
    print(i.ljust(20),data[i])



bill=0 
while True:
    product = input('enter the product name or [E]xit:').lower()
    if product =='E' or product =='e':
        print('thanks for shopping')
        print('total bill:', bill)
        break
    else:
        quantity =int(input('enter the quantity:'))
        bill += data[product]*quantity    






    


       