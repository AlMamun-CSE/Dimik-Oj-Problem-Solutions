def fact(n):
    if n == 1: return 1
    return fact(n - 1) * n


def word_repeat(words):
    repeats = []
    checked = []
    for word in words:
        if word not in checked:
            repeats.append(words.count(word))
            checked.append(word)
    return repeats


t = int(input())
for i in range(t):
    words = input().split(' ')
    word_count = len(words)
    repeats = word_repeat(words)
    minimizer = 1
    for n in repeats:
        minimizer *= fact(n)
    probability = fact(word_count) // minimizer
    print("1/%s" % probability)
