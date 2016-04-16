#interpolacja i aproksymacja pierwiastka
import math

from scipy.optimize import fsolve
from numpy.linalg import solve



import matplotlib.pyplot as pl
import numpy as np

x=np.linspace(-2.5,2,101)
y=x**5-8*x+17
y1=0*x

pl.plot(x,y,x,y1)



def f(x):
    return x**5-8*x+17
    
x1=fsolve(f,-2)
print(x1,f(x1))

p5=[1,0,0,0,-8,17]


print(np.roots(p5))

a = np.array([[3,2,7], 
              [7,-3,2],
              [-6,2,-3]])
b = np.array([5,7,9])
x = np.linalg.solve(a, b)
#lub
y=solve(a,b)

print(x,y)


a = np.array([[5,2,7], 
              [7,-3,2],
              [-6,2,-3]])
b = np.array([5,7,9])
x = np.linalg.solve(a, b)
#lub
y=solve(a,b)

print(x,y)

a = np.array([[7,-3,2], 
              [7,-3,2],
              [-6,2,-3]])
b = np.array([5,7,9])
x = np.linalg.solve(a, b)
#lub
y=solve(a,b)

print(x,y)