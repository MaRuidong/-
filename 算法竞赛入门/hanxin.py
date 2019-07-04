#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: hanxin.py
@time: 2019/7/4 21:26
@desc:
'''

def result(a,b,c):
    if a>=3 and b >= 5 and c >= 7:
        return None
    for n in range(10,101):
        if n %3 == a and n%5==b and n%7==c:
            return n
    return 'No answer'

print(result(2,1,3))