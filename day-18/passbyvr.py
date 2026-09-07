#PASS BY VALUE:it make changes only inside the function [immutable data types]
#PASS BY REFERENCE:it make changes in and outside the function [list ,set,dictionary]

#int float complex string tuple bool

'''def display(n):
    n+=12
    print('inside the function:',n)

n=10
display(n)
print('outside the function:',n) ''' 


'''def display(n):
    n+=12.3
    print('inside the function:',n)

n=10.3
display(n)
print('outside the function:',n)  '''  


'''def display(n):
    n+=12
    print('inside the function:',n)

n=10+3j
display(n)
print('outside the function:',n)    '''


'''def display(n):
    n=True
    print('inside the function:',n)

n =False
display(n)
print('outside the function:',n)   '''

'''def display(n):
    n+='lang'
    print('inside the function:',n)

n='python'
display(n)
print('outside the function:',n)  '''



'''def display(n):
    n+=(5,6)
    print('inside the function:',n)

n=(1,2,3,4)
display(n)
print('outside the function:',n)  '''


def display(n):
    n.append(5)
    print('inside the function:',n)

n=[1,2,3,4]
display(n)
print('outside the function:',n)  '''




