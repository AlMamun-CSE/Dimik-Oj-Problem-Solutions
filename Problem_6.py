def calculate_sum(n):
    last_and_first_index_sum = 0
    length = len(n)
    last_and_first_index_sum = int(int(n[0]) + int(n[length-1]))
    return last_and_first_index_sum


t = int(input())
for i in range(t):
    n = input()
    output = calculate_sum(n)
    print("Sum = %d" % output)


