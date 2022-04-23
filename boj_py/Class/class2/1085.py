x, y, w, h = map(int, input().split())
print(min(x, w - x, y, h - y))

# y != 0이면 x ^ 2 + y ^ 2 > x ^ 2이라