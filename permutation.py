# -*- coding:utf8 -*-

"""
输出全排列 例如
输入字符串abc，则打印出 a、b、c所能排列出来的所有字符串
abc、acb、bac、bca、cab 和 cba
如果输入的字母相同，考虑去重
"""


def is_swap(input_str, beg, end):  # 去重
    for j in xrange(beg, end):
        if input_str[j] == input_str[end]:
            return False
    return True


def permutation(input_str, beg, length):
    if beg == length - 1:
        print input_str

    else:
        for i in xrange(beg, length):
            if is_swap(input_str, beg, i):
                input_str[beg], input_str[i] = input_str[i], input_str[beg]
                permutation(input_str, beg+1, length)
                input_str[beg], input_str[i] = input_str[i], input_str[beg]


permutation(['a', 'b', 'c'], 0, 3)

permutation(['a', 'b', 'b'], 0, 3)

permutation(['b', 'b', 'b'], 0, 3)
