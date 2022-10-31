def fib(n):

    a = (1 + 5 ** 0.5) / 2
    b = (1 - 5 ** 0.5) / 2
    return (a ** n - b ** n) / 5 ** 0.5

n = int(input('N Fibonacci number: > '))
print(f'Result is: {int(fib(n))}')

