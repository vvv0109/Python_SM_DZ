import random
a=int(input("Введи степень: "))
q=a
d=''
z=-3
n=0
new_list=[]
new2_list=[]
new5_list=[]
new6_list=[]
while q>-1:
    if(z>=0):
        s='+'
        t = random.randint(0, 1)
        if t == 1:
            t = '*x'
            if q == 1 or q == 0:
                if q == 1:
                    d = d + f'{s}{z}{t}'
                    new_list.append(f'{s}{z}{t}')
                    new5_list.append(z)
                    n=n+1
                if q == 0:
                    d = d + f'{z}'
                    new_list.append(f'{z}')
                    new5_list.append(z)
            else:
                d = d + f'{s}{z}{t}**{q}'
                new_list.append(f'{s}{z}{t}**{q}')
                new5_list.append(z)
        else:
            t = ''
            d = d + f'{s}{z}'
            new_list.append(f'{s}{z}')

            q = q + 1
    else:
        s = '-'
        z=z*-1
        t=random.randint(0,1)
        if t==1:
            t='*x'
            if q == 1 or q == 0:
                if q == 1:
                    d = d + f'{s}{z}{t}'
                    new_list.append(f'{s}{z}{t}')
                    new5_list.append(z*-1)
                if q == 0:
                    d = d + f'{s}{z}'
                    new_list.append(f'{s}{z}')
            else:
                d = d + f'{s}{z}{t}**{q}'
                new_list.append(f'{s}{z}{t}**{q}')
                new5_list.append(z*-1)
        else:
            t = ''
            d=d+f'{s}{z}'
            new_list.append(f'{s}{z}')
            q = q + 1
    q=q-1
    z = random.randint(-100, 100)
d=d+'=0'
print("1-е уравнение: ", d)
data=open('txt1', 'w')
data.writelines(d)
q=a
d=''
z=-3
while q>-1:
    if(z>=0):
        s='+'
        t = random.randint(0, 1)
        if t == 1:
            t = '*x'
            if q == 1 or q == 0:
                if q == 1:
                    d = d + f'{s}{z}{t}'
                    new2_list.append(f'{s}{z}{t}')
                    new6_list.append(z)
                if q == 0:
                    d = d + f'{z}'
                    new2_list.append(f'{z}')
                    new6_list.append(z)
            else:
                d = d + f'{s}{z}{t}**{q}'
                new2_list.append(f'{s}{z}{t}**{q}')
                new6_list.append(z)
        else:
            t = ''
            d = d + f'{s}{z}'
            new2_list.append(f'{s}{z}')
            q = q + 1
    else:
        s = '-'
        z=z*-1
        t=random.randint(0,1)
        if t==1:
            t='*x'
            if q == 1 or q == 0:
                if q == 1:
                    d = d + f'{s}{z}{t}'
                    new2_list.append(f'{s}{z}{t}')
                    new6_list.append(z*-1)
                if q == 0:
                    d = d + f'{s}{z}'
                    new2_list.append(f'{s}{z}')
            else:
                d = d + f'{s}{z}{t}**{q}'
                new2_list.append(f'{s}{z}{t}**{q}')
                new6_list.append(z*-1)
        else:
            t = ''
            d=d+f'{s}{z}'
            new2_list.append(f'{s}{z}')
            q = q + 1
    q=q-1
    z = random.randint(-100, +100)
d=d+'=0'
print("2-е уравнение: ", d)
data=open('txt2', 'w')
data.writelines(d)
#print(new_list)
#print(new2_list)
stringVal='x'
new3_list=(f"{[ x for x in new_list if stringVal in x ]}")
new4_list=(f"{[ x for x in new2_list if stringVal in x ]}")
print("Упращение 2-е уравнение: ", new3_list)
print("Упращение 1-е уравнение: ",new4_list)
#print(new5_list)
#print(new6_list)
if (a<len(new5_list)):
    del new5_list[a]
if (a<len(new6_list)):
    del new6_list[a]
new7_list = [x + y for x, y in zip(new5_list, new6_list)]
new8_list=[]
e=len(new7_list)
for i in range(len(new7_list)):
    w=new7_list[i]
    if w>0:
        new8_list.append(f'+{w}*x**{e}')
    if w < 0:
         new8_list.append(f'{w}*x**{e}')
    e=e-1
print(new8_list)
data=open('total', 'w')
data.writelines(new8_list)