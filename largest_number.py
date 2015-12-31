# -*- coding:utf8 -*-

"""
给定一个非负整数数组，将其排成尽可能大的数。由于最终结果可能非常大，所以返回sring型
例如：给定数组[9, 81, 6, 35, 3, 30]得到最大数 981635330
"""


def compare(x, y):
    try:
        a = int(x)
        b = int(y)
    except:
        raise
    x = str(x)
    y = str(y)
    x_len = len(x)
    y_len = len(y)
    if x_len == y_len:
        if a == b:
                return 0
        elif a > b:
                return 1
        else:
                return -1

    min_len = x_len
    if x_len > y_len:
            min_len = y_len

    for i in range(min_len):
            x_i = int(x[i])
            y_i = int(y[i])
            if x_i > y_i:
                    return 1
            elif x_i < y_i:
                    return -1
    i += 1

    if x_len > y_len:
        for j in range(i, x_len):
            for k in range(min_len):
                if int(x[j]) > int(y[k]):
                        return 1
                elif int(x[j]) < int(y[k]):
                        return -1
    else:
        for j in range(i, y_len):
            for k in range(min_len):
                if int(y[j]) > int(x[k]):
                        return -1
                elif int(y[j]) < int(x[k]):
                        return 1


def largest_number(num_arr):
    str_arr = [str(i) for i in num_arr]
    str_arr.sort(reverse=True, cmp=compare)
    str_sum = ''.join(str_arr)
    return int(str_sum)

if __name__ == "__main__":
    # num_arr = [9, 81, 815, 10, 811, 811]
    num_arr = [9, 81, 6, 35, 3, 30]
    # num_arr = [43, 435, 4354, 4353]
    # num_arr = [43, 435]
    sum_ret = largest_number(num_arr)
    print type(sum_ret)
    print '\n'
    print sum_ret
