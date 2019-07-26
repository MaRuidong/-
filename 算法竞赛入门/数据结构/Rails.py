#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Rails.py
@time: 2019/7/26 22:17
@desc:
'''
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque([])
    def push(self,p):
        self.stack.append(p)
    def pop(self):
        return self.stack.pop()
    def top(self):
        p = self.pop()
        self.push(p)
        return p
    def empty(self):
        if self.stack:
            return True
        return False
ok = True
stack = Stack()
def main():
    B = 1
    A = 1
    global ok
    n = int(input('请输入n:'))
    target = [0 for i in range(n+1)]
    for i in range(1,n+1):
        target[i] = int(input())
    while B <= n:
        if A == target[B]:
            A+=1
            B+=1
        elif stack.empty() and target[B] == stack.top():
            stack.pop()
            B+=1
        elif A<=n :
            stack.push(A)
            A+=1
        else:
            ok = False
            break
    print(ok)
if __name__ == '__main__':
    main()