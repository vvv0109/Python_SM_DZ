c = int(input('Введите число '))
n = lambda a, b:  a * b
f = 1
for i in range(c):
    i+=1
    f = n(f,i)
    print(f, end=' ')