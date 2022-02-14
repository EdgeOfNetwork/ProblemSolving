from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # 특수조건
    if n > 0: yield
    last: int = 0  # fib(0)
    next: int = 1  # fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # 제너레이터 핵심 반환문


if __name__ == "__main__":
    for i in fib6(50):
        print(i)