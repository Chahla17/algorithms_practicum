import timeit
def fib_eo(n):
    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        previous, fib_number = fib_number, previous + fib_number

    return 'even' if fib_number % 2 == 0 else 'odd' 
n = int(input('N Fibonacci number: > '))
#1print(f'Result is: {fib_eo(n)}')
time = timeit.timeit(lambda: fib_eo(n), number=1)
print(time)
