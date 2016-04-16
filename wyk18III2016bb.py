#lista

a=[1.0,2.0,3.0]
a.append(4.0)   #dopisanie do listy
print(a)
a.insert(2,4.5)
print(a)

print(len(a))
                #ten sam obiekt pod dwoma nazwami a i b
b=a
b[0]=5.0

print(a)
print(b)

            #a i c dwa rozne obiekty
c=a[:]
c[0]=1
print(a)
print(c)

  

a=[[1,2,3],\
    [4,5,6],\
    [7,8,9]]
print(a)
print(a[1])
print(a[1][2])
      # trzeba pamiętać że liczymy od zera



