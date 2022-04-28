stack = []
while True:
    n = input()
    if n == '0':
        break
    for i in n:
        stack.append(int(i)) #문자열을 낱개로 stack에 집어넣는다.
    print(stack)
    cnt = 0
    for i in range(len(stack), len(stack) // 2 + 1):
        print("hello")
        if len(stack) % 2 == 0: #짝수라면,
            if stack[i] == stack[len(stack) - i]:
                cnt += 1
                if cnt == len(stack) // 2:
                    print("yes")
                else:
                    print("no")
        else: #홀수라면
            if stack[i] == stack[len(stack) - i - 1]:
                cnt += 1
                if cnt == len(stack) // 2:
                    print("yes")
                else:
                    print("no")
