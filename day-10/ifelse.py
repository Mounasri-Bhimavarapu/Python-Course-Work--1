'''username=input('enter the username:')
password=input('enter the pasword:')
if username=='admin' and password=='admin123':
    print('login sucessful')
else:
    print('ivalid credentials')
    '''

'''bill=int(input('enter the bill:'))
if bill>99:
    print('final bill:',bill)
else:
    print('final bill + delivery charges',bill+30)
    '''    
products=['laptop','bag','bottle','pen']  
search_product=input('enter the search product:')
if search_product in products:
    print(f'{search_product}found') 
else:
    print('search_product not found')