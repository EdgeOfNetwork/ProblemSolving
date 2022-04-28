n = int(input())

for i in range(n):
    code = input()
    code = list(code)
    sum = 0
    cnt = 0
    for i in code:
        if i == "O":
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)


