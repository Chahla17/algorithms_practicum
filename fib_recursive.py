import timeit
def fib(n):
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input('N Fibonacci number: > '))
#print(f'Result is: {fib(n)}')
time = timeit.timeit(lambda: fib(n), number=1)
print(time)
