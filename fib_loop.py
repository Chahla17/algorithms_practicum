import timeit
def fib(n):

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        previous, fib_number = fib_number, previous + fib_number

    return fib_number

n = int(input('N Fibonacci number: > '))
#print(f'Result is: {fib(n)}')
time = timeit.timeit(lambda: fib(n), number=1)
print(time)
