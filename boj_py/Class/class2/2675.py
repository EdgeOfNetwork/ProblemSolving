import sys


n = int(input())

for _ in range(n):
    numb, text = sys.stdin.readline().split()
    text = list(text)
    numb = int(numb)
    sub_result = []
    for i in text:
        for j in range(numb): #횟수만큼
            sub_result.append(i)
    res = ''.join(sub_result)
    print(res)


