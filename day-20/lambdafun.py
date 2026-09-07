# lambda function syntax: var = lambda argument : expression


'''wish = lambda name:f"welcome to the course {name}"
print(wish('mounasri'))
print(wish('usha'))


gst = lambda price : price*0.18
print(gst(1000))
print(gst(2050))

avg = lambda a,b,c: (a+b+c)/3
print(avg(1,2,3))
print(avg(9,6,8))

iseven = lambda a :"even" if a % 2==0 else"odd"
print(iseven(3))
print(iseven(89))
print(iseven(37))

largest = lambda a,b,c : a if a>b and a>c else( b if b>c else c)
print(largest(12,34,56))
print(largest(125,934,568))
print(largest(121,369,576))

isvowel = lambda a :"vowel" if a  in ('aeiouAEIOU') else "cons"
print(isvowel("j"))
print(isvowel('e'))
print(isvowel('l')) '''

'''
l =[12,34,56,78]
update = list(map(lambda i : i+10 ,l))
print(update)                                    # map is used to update

t=(10,11,12,13,14)
discount = list(map(lambda i: i-i*0.3 ,t))
print(discount) '''


'''l =[11,31,56,79]
update = list(filter(lambda i : i % 2!=0,l))
print(update)                                    # filter is used to access particular elements from data based on given conditions

t=(10,11,12,13,14)
discount = list(filter(lambda i: i>10,t))
print(discount) '''

'''l =['mounasri@gmail.com' , 'mounasri@yahoo.com','mounasri@codegnan.com','mounasri@outlook.com' ]
res =  list(map(lambda i:i.split('@')[-1] .split('.')[0],l))
print(res) '''

'''from functools import reduce

l=[2,4,5,68,89,23]
res = reduce(lambda sum ,i: sum+i,l)
print(res)

res1 =reduce(lambda pro,i :pro*i,l)
print(res1) '''

'''seats ={'s1': True,
        's2':False,
        's3':False,
        's4':False,
        's5':True,
        's6':True}

avg = list(filter(lambda i :seats[i]!=True,seats))
print(avg)       '''


products = {'suagr':30,
            'dal':79,
            'rice':40,
            'eggs':20 }

'''res = list(filter(lambda i:products[i]>50,products)) 
print(res)   '''    

print(dict(sorted(products.items(),key= lambda i :i[1])))
print(dict(sorted(products.items(),key= lambda i :i[1], reverse = True)))