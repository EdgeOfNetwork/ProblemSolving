numbers = []
for i in range(3):
    numbers.append(int(input()))

result = numbers[0] * numbers[1] * numbers[2]

result = str(result)

count = [0] * 10

for i in result:
    if i == '0':
        count[0] += 1
    elif i == '1':
        count[1] += 1
    elif i == '2':
        count[2] += 1
    elif i == '3':
        count[3] += 1
    elif i == '4':
        count[4] += 1
    elif i == '5':
        count[5] += 1
    elif i == '6':
        count[6] += 1
    elif i == '7':
        count[7] += 1
    elif i == '8':
        count[8] += 1
    elif i == '9':
        count[9] += 1

for i in count:
    print(i)