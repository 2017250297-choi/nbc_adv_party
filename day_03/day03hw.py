def pascal(n):
    if n == 1:
        return [1]
    else:
        ex_list = pascal(n - 1)
        newlist = [ex_list[i] + ex_list[i - 1] for i in range(1, len(ex_list))]
        return [1] + newlist + [1]


print(pascal(8))  # [1, 7, 21, 35, 35, 21, 7, 1]
