def fib(n : int) -> int: #type hinting
    #print(n)
    if n < 2: # base case
        return n
    return fib(n-1) + fib(n-2) # recursive case

if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
    print(fib(50))

