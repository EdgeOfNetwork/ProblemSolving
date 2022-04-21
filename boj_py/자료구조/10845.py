import sys

"""
TODO : push에서 밀어넣는 과정에서 [1, 2, 3] -> [1, 1, 2, 3] -> [4, 1, ,2, 3] 이렇게 짜보고 싶은데 i+1 = i 하는 과정이 도저히 안된다.
일단 패배선언을 때리지만 나중에 다시 해보자
일반적인 해설은 stack처럼 일단 밀어넣고 pop에서 dequeue처리를 한다.
"""


class QUEUE:
    def __init__(self):
        self.queue_list = []

    def empty(self):
        if len(self.queue_list) == 0:
            return 1
        else:
            return 0

    def push(self, x):
        self.queue_list.append(x)

    def pop(self):
        if self.empty() == 1:
            print(-1)
        else:
            print(self.queue_list[0]) #제일 앞에 있는것
            self.queue_list = self.queue_list[1:]

    def size(self):
        print(len(self.queue_list))

    def front(self):
        if self.empty() == 1:
            print(-1)
        else:
            print(self.queue_list[0]) #제일 앞엣놈 출력
    def back(self):
        if self.empty() == 1:
            print(-1)
        else:
            print(self.queue_list[-1])


n = int(input())
q = QUEUE()

for i in range(n):
    code = sys.stdin.readline()
    if 'push' in code:
        item = int(code[5:])
        q.push(item)
    elif 'pop' in code:
        q.pop()
    elif 'size' in code:
        q.size()
    elif 'empty' in code:
        print(q.empty())
    elif 'front' in code:
        q.front()
    elif 'back' in code:
        q.back()