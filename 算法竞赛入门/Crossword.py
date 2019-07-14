#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Crossword.py
@time: 2019/7/11 22:25
@desc:
'''
'''
思路:
    定义网格，定义向量，及上下左右移动的值
    遍历整个网格，找出所有的起始点，存储在eligible，
    存储横向单词和竖向单词的起始点在eligible中的位置，记为across和down
    遍历across和down，输出单词
'''
R = 6
N = 7
grid = [
    ['a','b','c','*','y','u','o'],
    ['*','d','e','*','c','x','g'],
    ['m','a','i','n','*','b','l'],
    ['y','u','*','r','h','q','n'],
    ['*','w','t','*','z','x','*'],
    ['a','d','s','*','v','r','u']
]
class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def vaild(p):
    if p.x >= 0 and p.x < R and p.y >= 0 and p.y < N :
        return True
    return False

def add(p1,p2):
    return Vector(p1.x+p2.x,p1.y+p2.y)

def main():
    across = []
    down = []
    eligible = []
    dUp = Vector(-1,0)
    dDown = Vector(1,0)
    dLeft = Vector(0,-1)
    dRight = Vector(0,1)

    for i in range(R):
        for j in range(N):
            if grid[i][j] == '*': continue
            p = Vector(i,j)
            left = add(p,dLeft)
            up = add(p,dUp)
            isCross = ( not vaild(left)) or (grid[left.x][left.y] == '*')  #找出横向单词起始点
            isDown = (not  vaild(up)) or (grid[up.x][up.y] == '*')    #找出竖向单词起始点
            if isCross : across.append(len(eligible))
            if isDown: down.append(len(eligible))
            if isCross or isDown : eligible.append(p)

    print('Across:\n')
    for n in across:
        word = ''
        p = eligible[n]
        while vaild(p) and grid[p.x][p.y] != '*':
            word = word+grid[p.x][p.y]
            p = add(p,dRight)
        print(n+1,word)

    print('Down:\n')
    for n in down:
        word = ''
        p = eligible[n]
        while vaild(p) and grid[p.x][p.y] != '*':
            word = word + grid[p.x][p.y]
            p = add(p, dDown)
        print(n + 1, word)

if __name__ == '__main__':
    main()