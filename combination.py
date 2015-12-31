# -*- coding:utf8 -*-

"""
输出全组合，ab和ba算同一个。例如：
输入三个字符 a、b、c，则它们的组合有a b c ab ac bc abc
"""


def combination(input_str):
    if '' == input_str.strip():
        return
    len_str = len(input_str)
    n = 1 << len_str

    for i in xrange(1, n+1):
        for j in xrange(len_str):
            if i & (1 << j):
                print input_str[j],

        print ' ',


combination('abc')

