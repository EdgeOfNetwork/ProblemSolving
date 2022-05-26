n = int(input())

item_list = []
for _ in range(n):
    item_list.append(input())

item_list = list(set(item_list)) #중복단어 제거
item_list.sort(key=lambda x : (len(x), x))

for i in item_list:
    print(i)