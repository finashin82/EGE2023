'''
Перевод из десятичной системы счисления в двоичную
'''
x = int(input())
s = ''
while x > 0:
    s = str(x % 2) + s
    x = x//2
print(s)
