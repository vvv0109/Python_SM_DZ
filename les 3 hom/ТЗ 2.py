#Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
a=random.randint(10,15)
new_list=[]
new_list2=[]
for i in range(a):
    с = random.randint(3, 5)
    new_list.append(с)
print(new_list)
if (((a/2)%1)!=0):
    a=int(a/2)+2
else:
    a = int(a / 2) + 1
for i in range(1,a):
    e=new_list[i-1]
    r=new_list[-i]
    z=e*r
    new_list2.append(z)
print("Произведение пар чисел списка",new_list2)