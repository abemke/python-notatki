#interpolacja i aproksymacja
nmax=5  
n=1
a=[]

while n<nmax:
        a.append(1.0/n)
        print(a)
        n=n+1
        
print(a)

c=lambda x,y: x**2+y**2

print(c(1,2))

