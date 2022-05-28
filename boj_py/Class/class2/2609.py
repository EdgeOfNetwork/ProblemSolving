n, m = map(int, input().split())

def gcd(n, m):
    if m == 0 : return n
    else : return gcd(m, n % m)

res = gcd(n,m)
print(res)
print(n * m // res)