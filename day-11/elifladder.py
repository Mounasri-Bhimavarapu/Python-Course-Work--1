'''hr = int(input('enter the time:'))

if 5<=hr>=11:
    print('good morning')
elif 12<=hr>=16:
    print('good afternoon')
elif 17<=hr>=20:
    print('good evening')
elif 21<=hr>24:
    print('good night')
else:
    print('midnight sleep well')
    '''

budget=int(input('enter the budget:'))
if budget > 10000:
    print('cloud hosting') 
elif budget >5000:
    print('business hosting')
elif budget >2000:
    print('premium hosting')
else:
    print('single hosting')                        