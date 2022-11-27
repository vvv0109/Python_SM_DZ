print ("Привет! покажу сумму чисел в числе, введи число:")
a=float(input())
d=a*10
q = 0
b = 0
if (a<0):
    a=a*-1
if (d%10)!=0:
    f=1
    while (f/10)!=0:
        f = a*(10**q)
        q=q+1
        f=f%10
    a = a * 10 ** (q - 2)
while (a>0):
    i = a%10
    a =int(a/10)
    b = b + i
d=d/10
print ("Сумма чисел в числе" , d ,"=", int(b))

