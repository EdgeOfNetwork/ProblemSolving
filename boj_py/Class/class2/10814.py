n = int(input())


item_list = []
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    item_list.append((age, name))

item_list.sort(key=lambda x : x[0]) #age 비교

for i in item_list:
    print(*i)