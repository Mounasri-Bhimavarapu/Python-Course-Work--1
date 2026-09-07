data={
    'salt':25,
    'suagr':30,
    'rice':40,
    'coconut':40,
    'dal':20,
    'wheatflour':20,
    'butter':70,
    'bread':55,
    'eggs':80
}


for i in data:
    print(i.ljust(20),data)



products=input('enter the product:') .split()
print('----------Bill----------')
bill=0
for i in products:
    print(i.ljust(20),data[i])
    bill += data[i]
print('total bill'.ljust(20),bill)    







