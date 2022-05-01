h, m = map(int, input().split())

if m - 45 >= 0:
    print(h, m - 45)
else:
    if h == 0:
        h = 23
        print(h, 60 + m - 45)
    else:
        print(h - 1, 60 + m - 45)
