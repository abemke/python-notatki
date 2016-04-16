import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr
import numpy.linalg as npl
clear="\n"*100
print(clear)
n=3
A=npr.rand(n,n)
b=npr.randint(10,size=n)
xA=npl.solve(A,b)
B=np.transpose(A)
yB=npl.solve (B,b)
plt.plot(xA,yB,'o-r',yB,xA,'x-y')
plt.show()
