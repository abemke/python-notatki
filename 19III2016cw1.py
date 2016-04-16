import matplotlib.pyplot as plt #rysowanie
import numpy as np
import numpy.random as npr
import numpy.linalg as npl
import scipy.interpolate as scint #interpolacja

n=30


#suma liczb od 1 do n
b=np.arange(1, n+1, 1)
suma=sum(b)
print(suma)

#suma liczb od 2 do 2n
c=2*b
print(sum(c))


#iloczyn liczb 1/2 do 1/n
d=1/b
print(d)
iloczyn=np.prod(d)
print(iloczyn)


#suma kwadratw tych ułamkw
e=d**2
sumkakw=sum(e)-1
print(sumkakw)

#list 2n x

parzysta = 0
x = np.array(npr.rand(2*n))

for l in range(2*n):
    if parzysta == 0:
        x[l] = npr.rand()
        parzysta = 1
    elif parzysta == 1:
        x[l] = npr.randint(n)
        parzysta = 0
print(x)

#odwrucona lista x zapisana na y

y = np.array(npr.rand(2*n))
pom = 2*n-1
for l in range(2*n):
    y[l] = x[pom]
    pom = pom-1

print(y)

#wykres
plt.plot(x, y, '-k', x, y, 'o b')
plt.show()

#f) listy 2n x

i=0
x=[] #tworzymy pustą tablicę
for i in range(2*n):
    if i%2 == 0:    #reszta z dzielenia i przez 2 wynosi 0?
        x.append(npr.rand())    #liczby losowe z przedział☺u (0,1)
    elif i%2 == 1: #miejsca nieparzyste w tablicy
        x.append(npr.randint(10)) # liczby losowe z przedziału od 1 do 10
    i=i+1
print(x)

#g) odwrucona lista x zapisana na y

i=0
y=[]
for i in range(2*n):
    y.append(x[2*n-1-i])
    i=i+1
print(y)


y=x[:]
print(y)
y.reverse()
print(y)


#h)wykres

plt.plot(x, y, '-k', x, y, 'o b')
plt.show()
