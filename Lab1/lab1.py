import math
import sys

print('Шевчук Михаил ИУ5-51Б')
print('Введите А')

while True:
    try:
        a = float(input('A = '))
        break
    except ValueError:
        print('Некорректные данные!')
print('Введите B')

while True:
    try:
        b = float(input('B = '))
        break
    except ValueError:
        print('Некорректные данные!')

print('Введите C')

while True:
    try:
        c = float(input('C = '))
        break
    except ValueError:
        print('Некорректные данные!')

if a==0 and b==0 and c==0:
    print('Корень любой')
    print('The end')
    sys.exit()

if a == 0 and b != 0 :
    D = -1 * c/b
    if D >= 0:
        y1 = math.fabs(math.sqrt(D))
        y2 = -1 * math.fabs(math.sqrt(D))
        print(f'Корни уравнения: {y1}, {y2}')
    else:
        print('Корней нет(((')
    print('The end')
    sys.exit()
if a != 0 and b == 0 :
    D = -1 * c/a
    if D >= 0:
        t1 = math.fabs(math.sqrt(D))
        y1 =  math.fabs(math.sqrt(D))
        y2 = -1 * math.fabs(math.sqrt(t1))
        print(f'Корни уравнения: {y1}, {y2}')
    else: 
        print('Корней нет(((')
    print('The end')
    sys.exit()
if a == 0 and b == 0 and c != 0:
    print('Нет решений')
    print('The end')
    sys.exit()
D = b * b - 4 * a * c
if D < 0 :
    z = x = False
    print('Корней нет')
else:
    x1 = (-1 * b + math.fabs(math.sqrt(D)))/(2 * a)
    if x1 >= 0:
        y1 = math.fabs(math.sqrt(x1))
        y2 = -1 * math.fabs(math.sqrt(x1))
        z = True
    else:
        z = False
    x2 = (-1 * b - math.fabs(math.sqrt(D)))/(2 * a)
    if x2 >= 0:
        y3 = math.fabs(math.sqrt(x2))
        y4 = -1 * math.fabs(math.sqrt(x2))
        x = True
    else:
        x = False
    if z or x:
        print('Корни уравнения')
        if z:
            print(f'{y1}, {y2} ')
        if x:
            print(f'{y3}, {y4} ')
    else:
        print('Корней нет :(')
print('The end')