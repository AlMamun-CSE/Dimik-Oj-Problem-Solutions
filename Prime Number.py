def prime_number(a, b):
    li = [True] * 100002

    for x in range(0, 12, 2):
        li[x] = False
    li[1], li[2] = False, True
    for xx in range(3, 320, 2):
        for xy in range(xx*xx, 100002, xx):
            li[xy] = False
    count = 0
    for itr in range(a, b+1):
        if li[itr]:
            count += 1
    print(count)


T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    prime_number(a, b)