# while True:
#     n = input()
#     if n == '0':
#         break
#
#     length = len(n)
#     answer = 'yes'
#     for i in range(length // 2):
#         if n[i] != n[length - i - 1]:  #와우, 검사코드 쩐다
#             answer = 'no'
#             break
#
#     print(answer)
#맘에 드는 코드
while True:
    n = input()

    if n == '0':
        break

    if n == n[::-1]:
        print("yes")
    else:
        print('no')

#이렇게하면 파이썬으로는 되게 쉽게 풀 수 있다.