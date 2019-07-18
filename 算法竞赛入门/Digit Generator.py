#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Digit Generator.py
@time: 2019/7/5 22:45
@desc:
'''

def main():
    dict = {}
    for m in range(1,100000):
        n = y = m
        while y != 0:
            n += y%10
            y = int(y/10)
        if n in dict:
            if dict[n] > m:
                dict[n] = m
        else: dict[n] = m

    T = int(input('请输入次数：'))
    while True:
        if T == 0: break
        T -= 1
        n = int(input('请输入n：'))
        if n in dict:
            print(dict[n])
        else: print(0)

main()
