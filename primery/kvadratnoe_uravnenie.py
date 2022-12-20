'''
Решение квадратного уравнения
'''
from math import sqrt # Импорт модуля math и функции нахождения корня (sqrt)
a = int(input())
b = int(input())
c = int(input())
d = b**2-4*a*c # Находим дискриминант
if d < 0:
    print('Корней нет')
if d == 0:
    print ('Корень один: x= ', -b/(2*a))
if d >0:
    print('Два корня:')
    print('x1= ', format((-b+sqrt(d))/(2*a), '.2f')) # Вывод корня с ограничением цифр после запятой
    print('x2= ', format((-b-sqrt(d))/(2*a), '.2f'))