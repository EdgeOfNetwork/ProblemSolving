n = int(input())

ans = 0
row = [0] * n # [0][0][0]...[0]


def is_promising(x): #조건검사
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queen(x): #0
    global ans
    if x == n: #0 == 8
       ans += 1
       return

    else:
        for i in range(n):
            row[x] = i         #[x, i] 에 퀸을 놓음
            if is_promising(x):
                n_queen(x + 1)


n_queen(0)
print(ans)