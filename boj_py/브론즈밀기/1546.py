
n = int(input())

numbers = list(map(int, input().split()))

#numbers.

sum = 0
for i in numbers:
    sum += i

print(sum // n)