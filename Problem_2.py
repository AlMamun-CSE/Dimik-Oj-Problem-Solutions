# N = int(input())
# for i in range(N):
#     a = int(input())
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# Another Way Solve This Problem
N = int(input())
for i in range(N):
    sample_str = input()
    # Get last character of string i.e. char at index position -1
    last_char = sample_str[-1]
    last_char = int(last_char)
    if last_char % 2 == 0:
        print("even")
    else:
        print("odd")