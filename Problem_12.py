# n = int(input())
# for i in range(n):
#     number = int(input())
#     zero_count = 0
#     while number >= 0:
#         mod = number % 10
#         if mod == 0:
#             zero_count += 1
#         elif mod == 1:
#             break
#         number -= 1
#     print(zero_count)

n = int(input())
for i in range(n):
    number = int(input())
    zero_count = 0
    x = 5
    while x <= number:
        zero_count += number // x
        x *= 5
    print(zero_count)