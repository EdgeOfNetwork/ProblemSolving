n = int(input())

for i in range(n):
    code = input()
    code = list(code)

    sum = 0
    cnt = 0

    for i in code:
        if i == "O":
            cnt += 1
            sum += cnt
        else:
            cnt = 0

    print(sum)


