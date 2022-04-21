#Stack -
import sys


class STACK:
    def __init__(self):
        self.stack_list = []

    def push(self, x):
        self.stack_list.append(x)

    def size(self):
        print(len(self.stack_list))

    def empty(self):
        if len(self.stack_list) == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty() == 1:
            print(-1)
        else:
            print(self.stack_list[-1])

    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            item = self.stack_list.pop()
            return item



n = int(input())
s = STACK()

for i in range(n): #n번만큼 돌기
    code = sys.stdin.readline()

    if 'push' in code:
        x = int(code[5:])
        s.push(x)

    elif 'top' in code:
        s.top()

    elif 'size' in code:
        s.size()

    elif 'empty' in code:
        print(s.empty())

    elif 'pop' in code:
        print(s.pop())

"""
TODO :
1. 클래스 설계
2. input numb 받기
2. While문 돌리고
- 명령문 받아 ,
-스택에 숫자 쌓기
- push 빼고 나머지는 print문 출력


"""
