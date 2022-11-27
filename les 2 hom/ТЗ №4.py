import numbers
import random
from copy import copy
a=random.randint(10,100)
new_list=[]
for i in range(a):
    с = random.randint(1000, 9999)
    new_list.append(с)
#new_list=[4064, 3338, 1263, 5711, 4064]
print( "1 этап: ", new_list)
new4_string=[]
q=1
u=0
i=0
r=0
while r<=a*4-1:
    c = new_list[i]
    s =int(c/(1000/q)%10)
    new4_string.append(s)
    q = q*10
    r=r+1
    if(q==10000):
        q=1
        i=i+1
#print(new4_string)
r=0
s = 0
z = 0
w=len(new4_string)
new5_string=[]
new_string1=[]
new5_string=copy(new4_string)
while r<w:
    c = new5_string[r]
    if 2<c<4:
        del new5_string[r]
        z=1
        s=1
    if s==1:
        new_string1.append(1)
        #new_string1.append(0)
    else:
        new_string1.append(0)
    r=r+1-z
    w=w-z
    z=0
    s=0
#print(new5_string)
#print(new_string1)
new_string2=[]
w=len(new4_string)
r=0
#print(new4_string)
while r<w:
    c = new4_string[r]
    z = new_string1[r]
    if (z<1):
        q = str(c)
        new_string2.append(q)
    else:
        new_string2.append("X")
        #new_string2.append(q)
    r=r+1
#print(new_string2)
w=len(new4_string)
r=0
z=0
new_string3=[]
while r<w:
    c = new_string2[r]
    r = r + 1
    s = new_string2[r]
    r = r + 1
    e = new_string2[r]
    r = r + 1
    i = new_string2[r]
    r = r + 1
    if (c!="X"):
        c=c
    else:
        c=""
    if (s!="X"):
        s=s
    else:
        s=""
    if (e!="X"):
        e=e
    else:
        e=""
    if (i!="X"):
        i=i
    else:
        i=""
    q = (c+s+e+i)

    new_string3.append(q)
print('2 этап:' , new_string3)
w=len(new4_string)
r=0
z=0
new_string7=[]
while r<w:
    c = new_string2[r]
    r = r + 1
    s = new_string2[r]
    r = r + 1
    e = new_string2[r]
    r = r + 1
    i = new_string2[r]
    r = r + 1
    if (c!="X"):
        c=int(c)
    else:
        c=0
    if (s!="X"):
        s=int(s)
    else:
        s=0
    if (e!="X"):
        e=int(e)
    else:
        e=0
    if (i!="X"):
        i=int(i)
    else:
        i=0
    q = c+s+e+i
    q=int(q)%10
    new_string7.append(q)
print("3 этап", new_string7)
temp = []
for x in new_string7:
    if x not in temp:
        temp.append(x)
new_string7 = temp
print("4 этап", new_string7)
