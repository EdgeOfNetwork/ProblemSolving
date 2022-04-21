n, m = input().split()

n = int(n[:: -1])
m = int(m[:: -1]) #역순

print(n) if n > m else print(m)
