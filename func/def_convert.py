# Функция перевода числа из 10 в любую систему счисления (2, 8, 16)

def convert(x, y):
    s = ''
    while x > 0:
        s = str(x % y) + s
        x = x // y
    return(s)