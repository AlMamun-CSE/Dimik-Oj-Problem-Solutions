T = int(input())
for i in range(1, T + 1):
    string = input()
    char = input()
    if char not in string:
        print("'%s' is not present" % char)
        continue
    c = 0
    for j in string:
        if j in char:
            c += 1
    print("Occurrence of '%s' in '%s' = %d" % (char, string, c))
