import matplotlib.pyplot as plt #rysowanie
import numpy as np
import numpy.random as npr
import numpy.linalg as npl
import scipy.interpolate as scint #interpolacja

w4=[2,4,0,1,7]  #definicja wielomianu
print(w4)
x3=np.polyval(w4,3) #wyliczenie wartości wielomianu w4 dla x=3
print(x3)
x=np.linspace(-4,4,101) #tworzy liste od -4 do 4 punktow 101; dziedzina
y=np.polyval(w4,x)
plt.plot(x,y , '-k', 3, x3, 'o b')
plt.show()

#suma wspolczynnikw wielomianu i ich iloczyn
w2=[3,-1,3]
print(w2)
suma=sum(w2)
iloczyn=np.prod(w2)
print(suma)
print(iloczyn)

#suma wileomianow w4 i w2
