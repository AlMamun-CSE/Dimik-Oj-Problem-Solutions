T = int(input())
for i in range(T):
    string = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in alphabet:
        if char in string:
            total = string.count(char)
            print("%s = %d" % (char, total))
    if i < T - 1:
        print()
