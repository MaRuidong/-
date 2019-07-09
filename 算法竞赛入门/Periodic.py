#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Periodic.py
@time: 2019/7/9 22:31
@desc:
'''

def periodic(s,p):
    if len(s)%len(p) != 0:
        return False
    for i in range(len(p),len(s)):
        if s[i] != p[i%len(p)]: return  False
    return True

def main(s):
    length = len(s)
    ans = 0
    for i in range(1,length):
        if periodic(s,s[:i+1]): return s[:i+1]
if __name__ == '__main__':
    s = input('请输入字符串：')
    print(main(s))