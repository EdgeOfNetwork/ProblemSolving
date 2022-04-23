M = int(input())

listed = []
for i in range(1, M + 1):
    listed_i = sum(map(int, str(i)))

    if M == i + listed_i:
        print(i) #1부터 올라가므로, 챠피 가장 작은 수를 내뱉는다.
        break #아 여기서 끊어줘야 좋겠구나
    if i == M: #생성자 i 와 입력값이 같다? 생성자가 없다
        print(0)


