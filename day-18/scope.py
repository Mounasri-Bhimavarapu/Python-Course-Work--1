#LOCAL VARIABLE: called within in the function.


'''def display():
    n=10
    print('inside function:',n)

display()
print('outside function:',n)    '''



# GLOBAL VARIABLE: Can be used both inside and out side the function.



'''def display():
    
    print('inside function:',n)

n=10
display()
print('outside function:',n)   ''' 

#global keyword is used to acces local variable globally


'''def display():
    global n
    n=10
    print('inside function:',n)

display()
print('outside function:',n)  ''' 


# once global variable is declared that variable should not be pass as parameter.

'''def display(n):
    global n
    n=10
    print('inside function:',n)

display(n)
print('outside function:',n)  ''' 



'''def display():
    course ='PFS'
    def update():
        course ='JFS'
        print('inside function:',course)

    update()
    print('outside function:',course) 
display()   '''    


#NON LOCAL: Used to acces the inside and ouside function[only function] where as global  used for entire file.


'''def display():
    course ='PFS'
    def update():
        nonlocal  course
        course ='JFS'
        print('inside function:',course)

    update()
    print('outside function:',course) 
display()       '''



# If we use built in method/function as variable , the function looses its actual scope and acts as a variable.


'''l=[1,2,3,4,5]
print(sum(l))

sum=20
print(sum) '''
