'''
Факториал числа n
'''
def f(n):
    if n ==1 :
        return 1
    else :
        return (f(n-1) * n)