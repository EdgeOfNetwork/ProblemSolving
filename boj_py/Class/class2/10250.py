n = int(input())

def search_room(h, w, n):
    num = n // h + 1
    floor = n % h
    if n % h == 0:
        num = n // h
        floor = h
    print(f'{floor * 100 + num}')

for _ in range(n):
    h, w, n = map(int, input().split())
    search_room(h, w, n)
