n = int(input())

def factorial(n, res):
    if n == 0:
        return res
    res *= n
    n = n - 1
    return factorial(n, res)

initial_numb = 1
res = list(str(factorial(n, initial_numb)))
res = res[::-1] #순서 뒤집기


cnt = 0
for i in res:
    if i == '0' :
        cnt += 1
    else:
        break

print(cnt)
