n, m = map(int, input().split())

i = 2
while True:
    if n % i == 0  and m % i == 0 :
        print(i)
        break
    i += 1
