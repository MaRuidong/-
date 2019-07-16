#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: DNA Consensus.py
@time: 2019/7/14 23:24
@desc: 习题3-7，DNA序列，求一个新的序列到所有其他序列的Hamming和最小
'''

import sys
DNA = [
    'TATGATAC',
    'TAAGCTAC',
    'AAAGATCC',
    'TGAGATAC',
    'TAAGATGT'
]
m = n = 0
def Hamming(s1,s2):
    dis = 0
    for i in range(n):
        if s1[i] == s2[i]: continue
        dis += 1
    return dis

def dictOrder(t,i):
    for j in range(len((DNA[t]))):
        if DNA[t][j] < DNA[i][j]:
            return t
        else:
            return i
    return t
def main():
    global m,n
    n = int(input('请输入DNA序列长度：'))
    m = int(input('情书如DNA序列数量：'))
    # for i in range(m):
    #     s = input('DNA序列：')
    #     DNA.append(s)

    min = sys.maxsize
    t = -1
    result = [[-1 for i in range(m)] for j in range(m)]
    for i in range(m):
        for j in range(i,m):
            result[i][j] = Hamming(DNA[i],DNA[j])
            result[j][i] = result[i][j]
        if min > sum(result[i]):
            min = sum(result[i])
            t = i
        elif min == sum(result[i]):
            min = dictOrder(t,i)
    print(result)
    print(DNA[t])

def main_new():
    global m, n
    n = int(input('请输入DNA序列长度：'))
    m = int(input('情书如DNA序列数量：'))
    dna = ''

    for j in range(n):
        max = -1
        key = ''
        dic = {'A':0,'C':0,'G':0,'T':0}
        for i in range(m):
            dic[DNA[i][j]] += 1
        for k in dic.keys():
            if dic[k] > max:
                max = dic[k]
                key = k
        dna = dna+key
    print(dna)


if __name__ == '__main__':
    main_new()