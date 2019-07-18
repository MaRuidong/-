#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Hangman.py
@time: 2019/7/18 21:45
@desc:
'''

chance = 6
length = -1
win = lose = 0
def guess(s,c):
    global chance,win,lose
    bad = 1
    n = s.find(c)
    if n != -1:
        s = s.replace(c,'')
        bad = 0
    if bad==1 : chance -= 1
    if len(s) == 0: win = 1
    if chance ==0: lose = 1
    return s

def main():
    while True:
        num = input('游戏编号（-1结束）：')
        if num == '-1': break
        s = input('单词：')
        s1 = input('猜测：')
        for c in s1:
            s = guess(s,c)
            if win == 1 or lose == 1:
                break
        if win == 1: print('You win!')
        elif lose == 1: print('You lose!')
        else: print('You checkened out!')

if __name__ == '__main__':
    main()