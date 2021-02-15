n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))[:3]
    arr.sort()
    output = ' '.join(str(i)for i in arr)
    print("Case %d:" % (i+1), output)
