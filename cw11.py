# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 09:04:21 2016

@author: Liberator
"""
# Importowanie bibliotek potrzebnych do działania funkcji i skrocenie ich nazw
import numpy as np
import matplotlib.pyplot as plt

# a) definiuje zmienna n rowna np. 101
n = 101

# b) buduje liste x, zawierajaca n rownoodleglych liczb z przedzialu (-2PI, 2PI)
x = np.linspace(-2*np.pi, 2*np.pi,n)

# c) oblicza liste s, zawierajaca sinusy liczb zawartych w liscie x
s = np.sin(x)

# d) oblicza liste c, zawierajaca cosinusy liczb zawartych w liscie x
c = np.cos(x)

# e) tworzy wykres funkcji sinus (linia ciagla zielona) i cosinus (linia
# czerwona przerywana), za pomoca list x, s, c
plt.plot(x, s, '-g', x, c, '--r')
plt.show()

# f) oblicza liste s2, zawierajaca kwadraty elementow listy s
s2 = s**2

# g) oblicza liste c2, zawierajaca kwadraty elementow listy c
c2 = c**2

# h) oblicza wektor jt, bedacysuma list s2 i c2
jt = s2 + c2

# i) oblicza zmienna sr, bedaca srednia elementow listy it
sr = np.mean(jt)

# j) wyswietla wartosc zmiennej sr za pomoca polecenia print
print(sr)