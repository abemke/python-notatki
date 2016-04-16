# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 09:04:21 2016

@author: Liberator
"""
# Importowanie bibliotek potrzebnych do działania funkcji i skrocenie ich nazw
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
import numpy.linalg as npl

# a) definiuje zmienna n rowna np. 3
n = 3

# b) buduje liste A o wymiarze n x n za pomoca polecenia rand
A = npr.rand(n,n)

# c) buduje n-elementowa liste b za pomoca polecenia randint
b = npr.randint(10,size=n)

# d) rozwiazuje uklad rownan Ax = b i wstawia wyniki do listy xA
xA = npl.solve(A,b)

# e) oblicza macierz B  bedaca transpozycja macierzy A
B = np.transpose(A)

# f) rozwiazuje uklad rownan Bx = b i wstawia wyniki do listy yB
yB = npl.solve(B,b)

# g) tworzy wykres, zawierajacy punkty wyznaczone przez odpowiednie elementy
# list xA i yB (kolka polaczone czerwona linia) oraz punkty wyznaczone przez
# odpowiednie elementy list yB i xA (krzyzyki polaczone zolta linia)
plt.plot(xA,yB,'o-r',yB,xA,'x-y')
plt.show()