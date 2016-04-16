import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr
import numpy.linalg as npl
clear="\n"*100
print(clear)

b=2  #b is integer type
print(b)
b=b*2.0     
print(b)
        #strings
string1='Press return to exit'
string2='the program'
print(string1+''+string2)   #concatenation
print (string1[0:10]) #Slicing

s= '3 9 81'
print(s.split())     #wynikiem lista trzech łańcuchow
#s[0]='p'  
        #tubki mieszają typy zmiennych

rec=('Smith','John',(6,23,68))  #this is a tuple
lastName,firstName,birthdate=rec
print(firstName)
birthYear = birthdate[2]
print(birthYear)


#lista

