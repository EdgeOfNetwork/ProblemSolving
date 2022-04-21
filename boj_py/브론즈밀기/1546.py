n = int(input())
numbers = list(map(int, input().split()))
max_numb = max(numbers)


def new_mean(numbers, max_numb):
    new_list = []
    for numb in numbers:
        new_list.append(numb / max_numb * 100)

    sum = 0
    for i in new_list:
        sum += i
    return round(sum / len(new_list), 2)

print(new_mean(numbers, max_numb))