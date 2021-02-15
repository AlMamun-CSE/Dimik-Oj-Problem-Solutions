
T = int(input())
for i in range(T):
    string = input()
    constant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowels = "aeiouAEIOU"

    v = ''
    c = ''
    for j in string:
        if j in vowels:
            v += j
        elif j in constant:
            c += j
    print(v)
    print(c)