#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
a = int(input('Введите десятичное число: ', ))
b = ''
while a > 0:
    b = str(a % 2) + b
    a = a // 2
print('Число в двоичной системе выглядит так  ', b)

# Или используем  встроенную функцию bin()

a = int(input('Введите десятичное число: ', ))
b = bin(a)
print('Число в двоичной системе выглядит так  ', b)
