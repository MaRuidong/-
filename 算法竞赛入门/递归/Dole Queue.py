#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Dole Queue.py
@time: 2019/7/18 23:47
@desc:
'''

q = [1,2,3,4,5,6,7,8,9,10]
k = 4
m = 3
n = len(q)
def go(p,d,t):
    while True:
        if t <= 0 : break
        p = (p + n + d ) % n
        while q[p] == 0:
            p = (p + n + d ) % n
        t -= 1
    return p

def main():
    p1 = 0
    p2 = n-1
    left = n
    while left > 0:
        p1 = go(p1,1,k)
        p2 = go(p2,-1,m)
        if p1 == p2:
            left -= 1
            print('The remove:{}'.format(q[p1]))
        else:
            left -= 2
            print('The remove:{},{}'.format(q[p1],q[p2]))
        q[p1] = q[p2] = 0
        if left > 0 :
            print(',')

if __name__ == '__main__':
    main()