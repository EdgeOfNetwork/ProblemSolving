length = int(input())
letters = input()

r = 31
M = 1234567891
sum = 0

ord_list = []
for i in letters:
    letter_converted_ord = ord(i) - 96
    ord_list.append(letter_converted_ord)


for i in range(0, length):
    converted_r = pow(r, i)
    res =  ord_list[i] * converted_r
    sum += int(res)

print(sum % M)