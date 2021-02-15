# Using recursion function
# Run Time Costly
# So, Another Way Using Loop than better


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input())
for i in range(n):
    s = int(input())
    # output = factorial(s)
    fact = 1
    for j in range(s, 1, -1):
        fact = fact * j
    print(fact)
    # print(output)

    # def n_factorial(number):
    #     if number == 1:
    #         return 1
    #     return number * n_factorial(number - 1)
    #
    #
    # n = int(input())
    # for i in range(n):
    #     number = int(input())
    #     result = n_factorial(number)
    #     print(result)
