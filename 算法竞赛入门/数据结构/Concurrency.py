#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Concurrency.py
@time: 2019/7/26 20:50
@desc:
'''
from collections import deque
qw = deque([])
q = deque([])
t = [0 for i in range(5)]
Q = 0
var = {}
lock = False

def run(cur):
    global lock
    rt = Q
    p = cur.copy()
    while rt > 0:
        s = cur.popleft()
        if s[2] == '=':
            rt -= t[0]
            w = int(s[4])
            if len(s) == 6:
                w = w*10+int(s[5])
            var[s[0]] = w
        elif s[2] == 'i':
            rt -= t[1]
            print(s[6]+','+str(var[s[6]]))
        elif s[2] == 'c':
            rt -= t[2]
            if lock:
                qw.append(cur)
                return
            else: lock = True
        elif s[2] == 'l':
            rt -= t[3]
            lock = False
            if qw:
                q.appendleft(qw.popleft())
        else:
            return
    if cur:
        q.append(cur)


def main():
    global Q
    cas = int(input('执行次数:'))
    while cas > 0:
        cas -= 1
        n = int(input('请输入n:'))
        for i in range(5):
            t[i] = int(input())
        Q = int(input('请输入Q:'))
        for i in range(n):
            program = deque([])
            while True:
                s = input()
                program.append(s)
                if s == 'end': break
            q.append(program)
        while q:
            cur = q.popleft()
            run(cur)

if __name__ == '__main__':
    main()