import random
a=int(input("Введи степень: "))
q = a
d = ''
z = -3
p=a
def fun (z):
    while q>-1:
        if(z>=0):
            s='+'
            t = random.randint(0, 1)
            if t == 1:
                t = '*x'
                if q == 1 or q == 0:
                    if q == 1:
                        d = d + f'{s}{z}{t}'
                    if q == 0:
                        d = d + f'{z}'
                else:
                    d = d + f'{s}{z}{t}**{q}'
            else:
                t = ''
                d = d + f'{s}{z}'
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
                    if q == 0:
                        d = d + f'{s}{z}'
                else:
                    d = d + f'{s}{z}{t}**{q}'
            else:
                t = ''
                d=d+f'{s}{z}'
                q = q + 1
        q=q-1
        z = random.randint(-100, +100)
    d=d+'=0'
    print(d)

