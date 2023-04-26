def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(4))  # 24


def fib(n):
    if 2 >= n:
        return n - 1
    return fib(n - 1) + fib(n - 2)


print(fib(5))  # 3


def pascal(n):
    if n == 1:
        return [1]
    else:
        ex_list = pascal(n - 1)
        newlist = [ex_list[i] + ex_list[i - 1] for i in range(1, len(ex_list))]
        return [1] + newlist + [1]


print(pascal(8))  # [1, 7, 21, 35, 35, 21, 7, 1]
