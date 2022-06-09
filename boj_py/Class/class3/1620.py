import sys

input = sys.stdin.readline
n, m = map(int, input().split()) #포캣몬 개수 , 내가 맞춰야 할 문제의 개수

items = {}

for i in range(1, n + 1):
    a = input().rstrip()
    items[i] = a
    items[a] = i

for i in range(m):
    exam = input().rstrip()
    if exam.isdigit():
        print(items[int(exam)])
    else:
        print(items[exam])

