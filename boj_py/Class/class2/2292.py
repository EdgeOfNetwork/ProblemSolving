n = int(input())

fib = 0
for i in range(0, 5000000):
    before = fib
    fib += i

    limit_under = before * 6
    limit = fib * 6 + 1

    if limit_under < n <= limit:
        print(i + 1)
        break