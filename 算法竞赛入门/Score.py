#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Score.py
@time: 2019/7/9 21:48
@desc:
'''

score = 0

def main(s):
    count = 0
    global score
    for c in s:
        if c == 'O':
            count += 1
        elif c == 'X':
            count = 0
        score = score+count
    print(score)

if __name__ == '__main__':
    s = input('请输入字符串：')
    main(s)
