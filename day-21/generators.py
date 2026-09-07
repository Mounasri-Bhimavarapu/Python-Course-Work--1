#GENERATORS : type of python function which gives values one at atime instaed of storing all at atime.we use "yield" keyword instead  of return

'''def reels() :
    data = ['1...100','101...200','201...300','301...400']
    for i in data:
        yield i

res=reels()

print(next(res))        
print(next(res))        
print(next(res))     '''


'''def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

res =countdown()
for i in res :
    print(i)     '''  # for loop directly supports generator function no need to use next


'''def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
res = factors(12) 
for i in res:
    print(res)     '''    


def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:    
                yield i
res = prime(100)
for i in res:
    print(i , end= " ")                
    
    

       
        


