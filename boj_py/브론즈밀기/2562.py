numbers = []
for i in range(9):
    numbers.append(int(input()))

print(max(numbers))

for i, numb in zip(range(len(numbers)), numbers):
    if numb is max(numbers):
        print(i + 1)