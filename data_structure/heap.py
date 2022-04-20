"""
TODO : 디버거 찍어보면서 어떻게 돌아가는지 관찰
TODO : 최대힙 제작해 볼 것
"""

class BHeap:
    def __init__(self, a):
        self.a = a
        self.N = len(a) - 1 # -1을 하는 이유는 [0]번째를 비우기 때문

    def create_heap(self):  #최소힙으로 만듬
        for i in range(self.N // 2, 0, -1): #
            self.downheap(i)

    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)

    def delete_min(self): # 최솟값을 쳐낸다는 뜻은 = down heap을 시작하는 과정
        if self.N == 0:
            print('힙이 비어있음')
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1] = self.a[1] #변수 교환 루트와 최솟값을 교환한다.
        del self.a[-1]
        self.N -= 1
        self.downheap(1) # 왜 1이 들어가는걸까?
        return minimum

    def downheap(self, i): #승자비교하며 힙속성 회복
        while 2 * i <= self.N:
            k = 2 * i
            if k < self.N and self.a[k][0] > self.a[k + 1][0]:
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k

    def upheap(self, j): #힙 올라가며 힙속성 회복
        while j > 1 and self.a[j // 2][0] > self.a[j][0]:
            self.a[j] , self.a[j // 2] = self.a[j // 2], self.a[j] #부모 자식 교환
            j = j // 2

    def print_heap(self): #힙 출력
        for i in range(1, self.N + 1):
            print('[%2d' % self.a[i][0], self.a[i][1],']', end='')
        print('\nheap size : ', self.N)


