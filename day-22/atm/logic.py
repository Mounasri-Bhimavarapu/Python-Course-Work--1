data ={
     123456:{'name':'mounasri','pin':1234,'balance':5000,'history':[]},
     234561:{'name':'usha','pin':1234,'balance':8000,'history':[]},
     345621:{'name':'lohitha','pin':1234,'balance':6000,'history':[]}, 
}

def login():
    global account_num
    account_num = int(input('enter the account number:'))
    pin =int(input('enter the pin:'))
    if account_num in data and data[account_num]['pin']==pin:
        print('login sucessfull')
        return True
    else:
        print('invalid login')

def menu():
    print(f"\nwelcome to the ATM ,{data[account_num]['name']}")
    print('[C]heck balancle')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transcation')
    print('[E]xit')


def checkbalance():
    print(f"\nhello{data[account_num]['name']},")
    print('current balance:',data[account_num]["balance"],end='\n\n')

def deposit():
    amount =int(input('enter the ammount:'))
    data[account_num]['balance']+=amount
    data[account_num]['history'].append(f'{amount}is deposited')
    print(f'{amount}is deposited sucessfully')

def withdraw():
    amount = int(input('enter the amount:'))
    if data[account_num]['balance']>=amount:
        data[account_num]['balance']-=amount
        data[account_num]['history'].append(f'{amount}is withdraw')
        print(f'{amount} is withdraw sucessfully')
        checkbalance()
    else:
        print('Insufficient Balance')   

def viewtransaction():
    if data[account_num]['history']:
        print('=======Transaction History======')
        for i in data[account_num]['history']:
            print(i)
        
        print('=========End of the History==========')
    else:
            print('No Transaction History') 
      


