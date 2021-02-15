def get_divisors(n):
    return [i for i in range(1, n + 1, 1) if (n % i == 0)]


t = int(input())
for c in range(t):
    n = int(input())
    output = ' '.join(str(i) for i in get_divisors(n))
    print("Case %s: %s" % (c + 1, output))
