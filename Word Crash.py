def word_cursh(s):
    return s[::-1]


T = int(input())
for i in range(T):
    string = input()
    lis = string.split()
    d = ' '
    for j in range(0, len(lis)):
        if j != len(lis) - 1:
            print(word_cursh(str(lis[j])), end=' ')
        else:
            print(word_cursh(str(lis[j])))
