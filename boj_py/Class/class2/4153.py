# li = []
#
# while 1:
#     x, y, z = map(int, input().split())
#     success = True if pow(x,2) + pow(y,2) == pow(z,2) else False
#
#     if x == 0 and y == 0 and z == 0:
#         for i in li:
#             print(i)
#         break
#     else:
#         if success == True:
#             li.append("right")
#         else:
#             li.append("wrong")

li = []

while True:
    A = list(map(int, input().split()))

    if A[0] == 0 and A[1] == 0 and A[2] == 0 :
        break
    maximum = max(A)
    A.remove(maximum)
    success = True if pow(A[0], 2) + pow(A[1], 2) == pow(maximum, 2) else False

    if success == True:
        print("right")
    else:
        print("wrong")