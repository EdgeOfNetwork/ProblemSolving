A = list(map(int, input().split()))

cnt = 0
for i in range(len(A) - 1):
    if A[i] + 1 == A[i + 1] :
        cnt += 1
        if cnt == 7:
            print("ascending")

    elif A[i] - 1 == A[i + 1] :
        cnt += 1
        if cnt == 7:
            print("decending")
print("mixed")