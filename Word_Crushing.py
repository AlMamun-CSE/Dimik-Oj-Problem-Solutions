T = int(input())
for i in range(T):
    string = input().split()
    for j in string:
        if j == " ":
            continue
        print(j[::-1], end=' ')
    print()


def reb(s):
    return s[::-1]


T = int(input())
for j in range(T):
    s = input()
    lis = s.split()
    string = ' '
    for i in range(0, len(lis)):
        if i != len(lis) - 1:
            print(reb(str(lis[i])), end=' ')
        else:
            print(reb(str(lis[i])))
