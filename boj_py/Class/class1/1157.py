# words = input().upper()
# unique_words = list(set(words))
# print(type(words))
#
# cnt_list = []
# for x in unique_words:
#     cnt = words.count(x) #count는
#     print(cnt)
#     cnt_list.append(cnt)
#
# if cnt_list.count(max(cnt_list)) > 1:
#     print("?")
# else:
#     max_index = cnt_list.index(max(cnt_list))
#     print(unique_words[max_index])

"""tip"""
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')

print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')


print('The index of i:', index)

# from collections import Counter
#
# input_string = input().upper()
# if len(input_string) == 1: print(input_string)
# else:
#     char_cnt = Counter(input_string).most_common(2)
#     #2개만 봐도 괜찮은 이유는,
#     #제일 많은애를 찾거나, 제일 적은애를 찾거나, 동일하다면 ?를 내보내면 되는 일이니 상관없다.
#     if char_cnt[0][1] == char_cnt[1][1]:
#         print("?")
#     else:
#         print(char_cnt[0][0]) #common앞에꺼가 더 큰거이므로
