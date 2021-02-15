T = int(input())
for i in range(T):
    string = input()
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    count = 0
    for j in string:
        if j in vowel:
            count += 1
    print("Number of vowels =", count)
