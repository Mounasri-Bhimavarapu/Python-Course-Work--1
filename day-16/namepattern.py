'''n = int(input('enter the size:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()     '''       



'''n = int(input('enter the size:'))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()          '''
        
        


'''n = int(input('enter the size:'))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1  or i==m:
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''        
                


'''n = int(input('enter the size:'))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 :
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()    '''                   





'''n = int(input('enter the size:'))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or i==m :
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''      



'''n = int(input('enter the size:'))

for i in range(n):
    for j in range(n):
        if   j==0 or i==n-1 :
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''          



'''n = int(input('enter the size:'))
m =n//2
for i in range(n):
    for j in range(n):
        if i==0 or  j==0 or i==n-1 or (j==n-1 and i>=m)or (j>=m and i==m) :
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print() '''               


'''n = int(input('enter the size:'))
m =n//2
for i in range(n):
    for j in range(n):
        if i==m or  j==0 or j==n-1  :
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()   '''                 



'''n = int(input('enter the size:'))
m =n//2
for i in range(n):
    for j in range(n):
        if j==m or  i==0 or i==n-1  :
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''                      



'''n = int(input('enter the size:'))
m =n//2
for i in range(n):
    for j in range(n):
        if j==m or  i==0 or (j<=m and i==n-1):  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()     '''      


'''n = int(input('enter the size:'))

for i in range(n):
    for j in range(n):
        if i==n-1 or  i==0 or j+i==n-1:  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()     '''          



'''n = int(input('enter the size:'))

for i in range(n):
    for j in range(n):
        if j==n-1 or  j==0 or j==i:  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()   '''                


'''n = int(input('enter the size:'))

for i in range(n):
    for j in range(n):
        if   j==i or j+i==n-1:  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''                     


'''n = int(input('enter the size:'))
m= n//2
for i in range(n):
    for j in range(n):
        if  ( j==i and i<=m) or j+i==n-1:  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()   '''              



'''n = int(input('enter the size:'))
m= n//2
for i in range(n):
    for j in range(n):
        if  ( j==i and i<=m) or (j+i==n-1 and j>=m):  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''               



'''n = int(input('enter the size:'))
m= n//2
for i in range(n):
    for j in range(n):
        if   j==0 or (i==m and j<=m)  or (j+i==n-1 and i<=m) or (i==j and i>=m):  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print() ''' 



'''n = int(input('enter the size:'))

for i in range(n):
    for j in range(n):
        if   j==0  or  j==n-1 or i==n-1:  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''



'''n = int(input('enter the size:'))
m = n//2
for i in range(n):
    for j in range(n):
        if   j==m  or  i==0 :  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''



'''n = int(input('enter the size:'))
m = n//2
for i in range(n):
    for j in range(n):
        if   (j==0 and j<=m ) or j==m or  i==0  or(j==n-1 and i>=m) or (i==n-1):  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''



'''n = int(input('enter the size:'))
m = n//2
for i in range(n):
    for j in range(n):
        if   (j==0 and i<=m  )or  i==0  or i==n-1 or(j==n-1 and i>=m ) or i==m:  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''




'''n = int(input('enter the size:'))
m = n//2
for i in range(n):
    for j in range(n):
        if  i==0 or j==0 or i==n-1 or j==n-1 or(i==j and i>=m):  
            print('*',end=' ')
        else :
            print(' ',end=' ')  
    print()  '''


'''n =int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or i-j==m or i+j==n+m-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''



'''n =int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==m or (j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''



'''n =int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and j<=m)or(j+i==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''



'''n =int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and j>=m)or(j+i==n-1 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() '''


'''n =int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==m or (j==n-1 and i<=m) or (i==j and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()   ''' 


n = int(input("Enter the number: "))
m = n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i>=m) or (j==n-1 and i>=m) or i+j==m or (j-i==m and j>=m) or i==m:
            print("*", end = " " )
        else:
            print(" ", end = " ")    
    print()    