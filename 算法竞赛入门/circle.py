#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: garner
@file: circle.py
@time: 2019/7/3 21:05
@desc:
'''

def circle(n):
    count = 0

    while n != 1:
        if n %2 == 0:
            n = n/2
        else:
            n = n*3+1
        count += 1
    return count

print(circle(3))