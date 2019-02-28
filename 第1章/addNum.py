# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:01:58 2019

@author: PC-CONFIG
"""
#两个二进制数相加
def addNum():
    A = [1,1,0]
    B = [0,1,0]
    C = [0]*4
    
    n = len(A)
    i = n-1
    flag = 0
    while i>=0:
        n = A[i]+B[i]+flag
        if n >= 2:
            C[i+1] = n-2
            flag = 1
        else:
            C[i+1] = n
            flag = 0
        i = i-1
    if flag == 1:
        C[0] = 1
    print('-',C)

addNum()