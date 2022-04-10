n = int(input())
numbers = list(map(int, input().split()))

max_numb = max(numbers)

print(max_numb)
numbers.remove(max_numb)

print(numbers)

sum = 0
for i in numbers:
    sum += i

print(sum)
print(len(numbers))

