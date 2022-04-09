n = list(input())

print(n)
cnt = 0

#입력받은 단어 전부 대문자로 변환

#알파벳 중복을 제거 후, 리스트에 뭐가 있는지 정도 체크

#들어있는 알파벳이 몇개 있는지 카운팅하는 함수

#카운팅 로직을 함수화


for i in range(len(n)):
    if n[i].isupper() == True:
        cnt += 1

        if cnt > 1:
            print("?")

    n[i].isupper()