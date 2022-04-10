# n = str(input()).upper() #입력받은 단어 전부 대문자로 변환
#
# #알파벳 중복을 제거 후, 리스트에 뭐가 있는지 정도 체크
# to_count = list(n)
# n = sorted(list(set(n))) #단어 중복 제거
#
# alpha_count = [0] * 26
#
# for i in range(len(to_count)):
#     if n.count()
#     if to_count[i] in n:
#
#         alpha_count[i] += 1 #특정단어의 카운트를 올리는 작업
#
# #들어있는 알파벳이 몇개 있는지 카운팅하는 함수
# #카운팅 로직을 함수화

from collections import Counter

input_string = input().upper()
if len(input_string) == 1: print(input_string)
else:
    char_cnt = Counter(input_string).most_common(2)
    #2개만 봐도 괜찮은 이유는,
    #제일 많은애를 찾거나, 제일 적은애를 찾거나, 동일하다면 ?를 내보내면 되는 일이니 상관없다.
    if char_cnt[0][1] == char_cnt[1][1]:
        print("?")
    else:
        print(char_cnt[0][0]) #common앞에꺼가 더 큰거이므로
