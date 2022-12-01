import random
a=random.randint(10,15)
new_list=[]
for i in range(a):
    с = random.randint(1, 100)
    new_list.append(с)
print(new_list)
z=0
for i in range(1,a,2):
    e=new_list[i]
    z=e+z
print("Сумма на нечётных позициях",z)

