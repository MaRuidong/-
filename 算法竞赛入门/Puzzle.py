#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Puzzle.py
@time: 2019/7/10 23:00
@desc:
'''


'''
思路：
    定义网格的向量，表示网格元素的坐标
    遍历指令集合，根据指令移动空格
'''
grid = [['' for i in range(5)] for j in range(5)]
Gsize = 4
class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
pos = Vector(-1,-1)
def add(p1,p2):
    return Vector(p1.x+p2.x,p1.y+p2.y)

def vaild(p):
    if p.x >= 0 and p.x < Gsize and p.y >= 0 and p.y < Gsize :
        return True
    return False

def move(c):
    m = None
    if c == 'A':    m = Vector(-1,0)
    if c == 'B':    m = Vector(1,0)
    if c == 'L':    m = Vector(0, -1)
    if c == 'R':    m = Vector(0, 1)
    return m

def main(cmds):
    global pos
    for c in cmds:
        if c == '0': return
        epos = add(pos,move(c))
        if not vaild(epos):
            print('This puzzle has no final configuration')
            return
        grid[pos.x][pos.y],grid[epos.x][epos.y] = grid[epos.x][epos.y],grid[pos.x][pos.y]
        pos = epos

if __name__ == '__main__':
    puzzle = input('请输入网格序列：')
    cmds = input('请输入指令序列：')
    for i in range(5):
        for j in range(5):
            grid[i][j] = puzzle[i*5+j]
            if puzzle[i*5+j] == ' ':
                pos.x = i
                pos.y = j

    main(cmds)
    print(grid)