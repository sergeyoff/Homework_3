# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
n = int(input('Введите длину ряда: '))
f1 = f2 = 1
print(f1, f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов var.2

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))
n = int(input('Введите длину ряда: '))
print('Последовательность Фибоначчи:')
for i in range(n):
    print(fib(i), end=' ')