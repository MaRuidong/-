#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: pailie.py
@time: 2019/7/4 21:41
@desc:
'''

visit = [True, True, True]
temp = ["" for x in range(0, 3)]


def dfs(position):
    if position == len(arr):
        print(temp)
        return

    for index in range(0, len(arr)):
        if visit[index] == True:
            temp[position] = arr[index]
            visit[index] = False
            dfs(position + 1)
            visit[index] = True


arr = ["a", "b", "c"]
dfs(0)
