#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Circular Sequence.py
@time: 2019/7/9 21:20
@desc:
'''
ans = 0
def less(s,p,q):
    for i in range(len(s)):
        if s[p+i] < s[q+i]:
            global ans
            ans = p
        elif s[p+i] > s[q+i]:
            break

def main(s):
    length = len(s)
    for i in range(1,length):
        less(s,i,ans)

    print(ans)
    print(s[ans:length]+s[0:ans])

main('CGAGTCAGCT')