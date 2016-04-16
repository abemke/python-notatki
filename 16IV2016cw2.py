import matplotlib.pyplot as plt #rysowanie
import numpy as np
import numpy.random as npr
import numpy.linalg as npl
import scipy.interpolate as scint #interpolacja
from scipy.optimize import fsolve
from numpy.linalg import solve
import scipy.linalg as sclin #wykorzystuje funkcja hilbert




#PSPI 2016 Python -cwiczenie 3
#zadanie 2
#a)
A=np.array([[npr.rand(),npr.rand(),npr.rand()],
            [npr.rand(),npr.rand(),npr.rand()],
            [npr.rand(),npr.rand(),npr.rand()]])
print(A)


#b)
b=np.array([npr.rand(),npr.rand(),npr.rand()])
print(b)
#c)
x=solve(A,b)
print(x)

#sprawdzenie poprawności rozwiązania
print(npl.norm(np.dot(A,x)-b))
# powinno wyjść coś bliskiego zeru

#d)
H=sclin.hilbert(4)
print(H)

#e)
c=np.array([npr.rand(),npr.rand(),npr.rand(),npr.rand()])
print(c)

#f)
y=solve(H,c)
print(y)

#sprawdzenie poprawności rozwiązania
print(npl.norm(np.dot(H,y)-c))
# powinno wyjść coś bliskiego zeru

#g

H=sclin.hilbert(7)
print(H)

c=np.array([npr.rand(),npr.rand(),npr.rand(),npr.rand(),npr.rand(),npr.rand(),npr.rand()])
print(c)

y=solve(H,c)
print(y)

#sprawdzenie poprawności rozwiązania
print(npl.norm(np.dot(H,y)-c))
# powinno wyjść coś bliskiego zeru
#dokł•adnośc błedu zmniejsza się


