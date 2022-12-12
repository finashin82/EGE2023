'''
На вход алгоритма подаётся натуральное число N.
Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. Далее эта запись обрабатывается по следующему правилу:
а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 0,
    а затем два левых разряда заменяются на 10;
б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 1,
    а затем два левых разряда заменяются на 11.
Полученная таким образом запись является двоичной записью искомого числа R.
Например, для исходного числа 6(10) = 110(2) результатом является число
1000(2) = 8(10), а для исходного числа 4(10) = 100(2) результатом является число 1101(2) = 13(10).
Укажите минимальное число N, после обработки которого с помощью этого алгоритма получается число R,
большее 40. В ответе запишите это число в десятичной системе счисления.
'''
# Импорт функции convert (перевод из 10 в 2, 8, 16)
# convert(x, y) x - данное число в 10 сист. счисл.
# y - основание сист. счисл. в которую нужно перевести
from func.def_convert import convert

for x in range(1,1000):

    y = convert(x,2) # Переводим в 2 сист. счисл.

    if y.count('1') % 2 == 0: # Если количество '1' в двоичном числе четное, то:
        y = y + '0' # Добавляем к строке справа '0'
        y = y[2::] # Удаляем первые (слева) два разряда
        y = '10' + y # Добавляем слева '10'
        if int(y, 2) > 40: # Переводим полученное число в 10 сист. счисл. и если оно > 40, вывод x и к.ц.
            print(x)
            break
    else:
        y = y + '1' # Добавляем к строке справа '1'
        y = y[2::] # Удаляем первые (слева) два разряда
        y = '11' + y # Добавляем слева '11'
        if int(y, 2) > 40: # Переводим полученное число в 10 сист. счисл. и если оно > 40, вывод x и к.ц.
            print(x)
            break

