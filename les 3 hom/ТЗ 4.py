#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import random
a=input()
a=int(a)
list=[]
while a>=0.9:
    a=(a/2)
    if a%1!=0:
        z=1
        list.append(z)
    else:
        z=0
        list.append(z)
    a =int(a)
list.reverse()
print(*list,)
