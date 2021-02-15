import math
n = int(input())
for i in range(n):
    num = int(input())
    square_root = math.sqrt(num)
    # print(square_root * square_root)
    if int(square_root) * int(square_root) == num:
        print("YES")
    else:
        print("NO")

# Another Way Solve This Problem

# def whole_squareNum(num):
#     ck = 0
#     if num == 1:
#         ck =1
#     else:
#         for i in range(2,int(num//2)):
#             if i * i == num:
#                 ck = 1
#                 break
#     if ck == 0:
#         print("NO")
#     elif ck == 1:
#         print("YES")
#
#
# n = int(input())
# for i in range(n):
#     num = int(input())
#     whole_squareNum(num)
