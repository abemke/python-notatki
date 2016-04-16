import matplotlib.pyplot as plt
import numpy as np
clear="\n"*100
print(clear)
n=101
x=np.linspace(-2*np.pi,2*np.pi,n)
s=np.sin(x)
c=np.cos(x)
plt.plot(x,s,'-g',x,c,'--r')
plt.show()
s2=s**2
c2=c**2
jt=s2+c2
sr=np.mean(jt)
print(sr)
