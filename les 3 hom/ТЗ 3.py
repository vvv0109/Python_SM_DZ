import random
new_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list2=[]
for i in range(len(new_list)):
    с = new_list[i]
    w=с
    u=w
    w=int(w)
    z=round(u-w, 5)
    if z==0:
        z='0'
    else:
        new_list2.append(z)
print(new_list2)
c=min(new_list2)
x=max(new_list2)
print("Разница остатка-", x-c)
