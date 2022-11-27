#Реализуйте алгоритм перемешивания списка.
#Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random
a=random.randint(5,10)
new_list=[]
for i in range(a):
    new_list.append(i)
print(new_list)
for i in range(a):
    c = random.randint(1, 5)
    u=new_list[c]
    b=new_list[i]
    new_list[i] = u
    new_list[c] = b
    i = i + 1
print(new_list)
