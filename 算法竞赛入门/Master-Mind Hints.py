#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Master-Mind Hints.py
@time: 2019/7/5 21:54
@desc:
'''

#算法导论第二版，例题3-4，猜数字游戏
def main():
    kase = 0
    while True:
        n = int(input('请输入n：'))
        if n == 0:
            break
        kase += 1
        print('游戏轮数{}'.format(kase))
        a = []
        for i in range(n): a.append(int(input()))

        while True:
            A = B = 0
            b = []
            for i in range(n):
                b.append(int(input()))
                if a[i] == b[i]: A += 1
            if b[0] == 0: break
            for d in range(1,10):
                c1 = c2 =0
                for i in range(n):
                    if a[i] == d: c1 += 1
                    if b[i] == d: c2 += 1
                if c1 < c2: B += c1
                else: B+=c2
            print('{} {}'.format(A, B - A))

main()
