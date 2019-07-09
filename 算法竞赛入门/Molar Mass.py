#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Molar Mass.py
@time: 2019/7/9 22:04
@desc:
'''

mass = float(0)
def main(s):
    W = {'C':12.01,'H':1.008,'O':16.00,'N':14.01}
    global mass
    count = 0
    now = 0
    for c in s:
        if c > '0' and c <= '9':
            mass += (int(s[count+1:now+1])-1) * W[s[count]]
        else:
            mass += W[c]
            count = now
        now += 1
    print(mass)

if __name__ == '__main__':
    s = input('请输入分子式：')
    main(s)