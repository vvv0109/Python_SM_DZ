import random
from random import randint, choice
def trc(a):
    q = randint(1,29)
    while a-q <= 28 and a > 29:
        q = randint(1,29)
    return q
a = int(150)
g = randint(0,2)
if g:
    print(f"Первый ходит player1")
else:
    print(f"Первый ходит player2")
w = 0
z = 0
while a > 28:
    if g:
        q = int(input('введите количество конфет:'))
        w += q
        a -= q
        g = 0
        print(f"Осталось на столе {a} конфет.")
    else:
        q = trc (a)
        z += q
        a -= q
        g = 1
        print(f"Робот взял и осталось на столе {a} конфет.")
if g==1:
    print(f"Ты выиграл")
else:
    print(f"Ты не выиграл")