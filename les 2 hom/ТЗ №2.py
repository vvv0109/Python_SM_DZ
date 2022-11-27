#Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.
import random
a=random.randint(5,10)
list=[]
n=1
s=0
for i in range(a):
    m=round((1 + 1/n)**n, 3)
    list.append(m)
    n=m
    s=s+m
print(list , "сумма ", m)