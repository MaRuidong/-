#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: All in ALL.py
@time: 2019/7/16 22:27
@desc:习题3-9 子序列
'''

def main():
    s = input('请输入字符串s:')
    t = input('请输入字符串t:')

    if len(t) < len(s) :
        print('输入不合法')
        return None
    i = 0
    for c in s:
        i = t.find(c,i,len(t))
        if i == -1: return False
    return True

if __name__ == '__main__':
    print(main())