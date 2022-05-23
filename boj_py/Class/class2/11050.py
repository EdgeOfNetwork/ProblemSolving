n, k = map(int, input().split())

n_res = 1


def factorial(numb, res):
    if numb == 0:
        return res
    res *= numb
    return factorial(numb - 1, res)

binominal = factorial(n, 1) / (factorial(k, 1) * factorial(n - k, 1))

print(int(binominal))