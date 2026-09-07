'''fa= eval(input('follow account:'))

if fa:
    cf=eval(input('close friend:'))
    if cf:
        print('story visible')
    else:
        print('not in close friends list')
else:
    print('follow the account first')
    ''' 

'''reg=eval(input('registred:')) 
if reg:
    fee=eval(input('Fee paid:'))
    if fee:
        print('tournament entry confirmied')
    else:
        print(' entry fee pending') 
else:
    print('registartion required') 
    '''                  

'''link_status=eval(input('enter the link status:'))
if link_status:
    pm=eval(input('pm status:'))
    if pm:
        print('permission granted')
    else:
        print('access denied')
else:
    print('invalid link')
    ''' 

data={'lohitha':{'status':'True','python':90,'mysql':95,'flask':96},
      'mounasri':{'status':'True','python':95,'mysql':90,'flask':70},
       'usha':{'status':'True','python':50,'mysql':60,'flask':35},
       'radha':{'status':'False','python':35,'mysql':55,'flask':35},
       'kiram':{'status':'True','python':70,'mysql':75,'flask':77},
       'dinesh':{'status':'True','python':80,'mysql':70,'flask':88},
       }

name=input('enter the name:')
if name in data:
    if data[name]['status']:
       sum = data[name]['python']+data[name]['mysql']+data[name]['flask']
       avg=sum/3
       print(f'hello {name}!!!')
       print(f'your average score is {avg}')
       if avg >= 90:
        print('excellent')
       elif avg >=80:
        print('verygood')
       elif avg >=75:
        print('good')
       elif avg >=60:
        print('work hard')
       elif avg >=35:
        print('better luck next time')
       else:
        print('failed exam')
    else:
        print(f'{name} did not attend exam') 
else:
    print(f'{name} not found in data')           


 
                          