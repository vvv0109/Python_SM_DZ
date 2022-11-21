#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
print ("Привет! Давай проверим истинность утверждения. Введи числа, где 0- лож, а 1-истина:")
print ("X=")
a=int(input())
print ("Y=")
b=int(input())
print ("Z=")
c=int(input())
if ((a and b and c)== 0 or (a and b and c)== 1):
    if ((a or b or c)== 0):
        q=1
    else:
        q = 0
#приводим правую часть
    if (a)== 0:
        w=1
    else:
        w = 0
    if (b) == 0:
        e = 1
    else:
        e = 0
    if (c) == 0:
        r = 1
    else:
        r = 0
    #расчёт правую часть
    if ((w*e*r)== 0):
        t=0
    else:
        t=1
    #сравнение
    if (t==q):
        print ("значение истина")
    else:
        print ("значение ЛОЖ")
else:
    print ("Значения принимаю только в двоичной СИ, где 0- лож, а 1-истина")
# ссылка на онл.калькулятор https://programforyou.ru/calculators/postroenie-tablitci-istinnosti-sknf-sdnf
