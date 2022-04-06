"""
2751 문제에서 메모리를 줄여야 하는 문제다.

출처 : https://somjang.tistory.com/entry/Mxmxmxm
"""

import sys

N = int(input())
check_list = [0] * 10001
# 0으로 가득찬 길이가 10,000인 list 생성 후 입력받는 수를 index로 하여
# 해당 index의 값을 1씩 증가해주고 해당 list를 처음부터 반복문을 돌면서
# 0이 아닐경우 해당 숫자만큼 해당 index를 출력하는 방법을 떠올려본다

for i in range(N):
    input_num = int(sys.stdin.readline())
    check_list[input_num] = check_list[input_num] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)

"""
충격적인 정렬방식이었다.

디버거를 사용해서 천천히 음미해보자
"""
