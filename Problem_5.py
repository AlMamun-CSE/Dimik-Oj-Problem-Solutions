def art_square(n):
    for i in range(n):
        print("*" * n)


T = int(input())
for i in range(T):
    n = int(input())
    art_square(n)
    # print() Wrong Answer But Last Loop Index Create New Line.So, Check
    if i != (T - 1):
        print('')
