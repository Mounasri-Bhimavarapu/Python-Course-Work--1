import logic as lg

if lg.login():
    while True:                                                   
        lg.menu()
        ch=input('enter the choice:').upper()
        if ch == 'C':
            lg.checkbalance()
        elif ch == 'D':
            lg.deposit()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'V':
            lg.viewtransaction()
        elif ch == 'E':
            print('-------thank you ,visit again--------')
            break
        else:
            print('enter the valid choice')                   




