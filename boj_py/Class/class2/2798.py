import itertools

n, m = map(int, input().split())
A = list(map(int, input().split()))

biggest_num = 0

for cards in itertools.combinations(A, 3):
    temp = sum(cards)
    if biggest_num < temp <= m: #개천재다
        biggest_num = temp #계속해서 조건에 맞는애를 업데이트

print(biggest_num)

#TODO : 속도 초과, 어떻게 해결할까

# def iter(nPr):
#     listed = []
#     for i in nPr:
#         listed.append(sum(i))
#         if sum(i) == m:
#             return sum(i)
#
#     listed.sort()
#     for i in range(1, m):
#         if m - i in listed:
#             return m - i
#
# nPr = itertools.permutations(A, 3)
# print(iter(nPr))