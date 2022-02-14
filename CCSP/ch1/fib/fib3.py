from typing import Dict
memo: Dict[int, int] = {0:0,1:1} #base case

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2) #memoization
    return memo[n]

if __name__ == "__main__":
    print(fib3(5))
    print(fib3(50))

    #오 메모이제이션을 썼더니 fib50 연산이 가능해진다
    # C++에서 const처럼 상수값을 지정해놓는 것 같다는 느낌을 받았다.
    # 변수 memo에 미리 계산된 요소가 있다면, 다시 계산하지 않고 결과를 반환한다.