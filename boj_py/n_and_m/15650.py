from itertools import combinations


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i + 1:], r - 1):
                yield [arr[i]] + next


n, m = map(int, input().split())

for item in combinations(range(1, n + 1), m):
    print(*item)
