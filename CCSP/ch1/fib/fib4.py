from functools import lru_cache

#함수를 자동으로 메모이징하는 내장형 데코레이터 존재
@lru_cache(maxsize=None) #캐시의 제한을 푼다
def fib4(n : int) -> int:
    if n < 2: # base case
        return n
    return fib4(n-1) + fib4(n-2)

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))