import matplotlib.pyplot as plt #rysowanie
import numpy as np
import numpy.random as npr
import numpy.linalg as npl
import scipy.interpolate as scint #interpolacja
from scipy.optimize import fsolve
from numpy.linalg import solve





#PSPI 2016 Python -cwiczenie 3
#a)
def f1(x):
    return np.sqrt((np.sin(x))**2+np.abs(x))-x**2

def f2(x):
    return (x-1)*(np.exp(2*x)-2*np.exp(x))

print(f1(1))
print(f2(2))

#b)
x=np.linspace(-1.3,1.3,101)
y1=0*x
plt.plot(x,f1(x) , '-k', x, f2(x), '-b',x,y1,'-g')
plt.show()

#c)
#miejsca zerowe dla funkcji f2
x02_1=fsolve(f2,0.7)
x02_2=fsolve(f2,1)
print(x02_1, x02_2)

#miejsca zerowe dla funkcji f1
x01_1=fsolve(f1,-1.2)
x01_2=fsolve(f1,0)
x01_3=fsolve(f1,1.2)
print(x01_1, x01_2, x01_3)

#punktu przecięcia
def f3(x):
    return f1(x)-f2(x)
    
x0_f1f2_1=fsolve(f3,0.3)
x0_f1f2_2=fsolve(f3,1.1)
print(x0_f1f2_1, x0_f1f2_2)

#wartości y dla pkt przecięcia:
y1_3=f3(0.33794812)
y2_3=f3(1.07493478)
print(y1_3,y2_3)



