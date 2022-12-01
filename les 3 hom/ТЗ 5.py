#Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
import random
a=random.randint(10,15)
new_list=[]
new_list2=[]
c=1
z=0
e=0
for i in range(a):
    x = c + z
    c=z
    z=x
    if(((i/2)%1)!=0):
        e = z * -1
        new_list.insert(0, e)
    else:
        e = z
        new_list.insert(0, e)
    new_list.append(z)
new_list.insert(a, 0)
print(new_list)