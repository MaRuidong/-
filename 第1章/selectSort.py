# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:52:53 2019

@author: PC-CONFIG
"""

#选择算法
def selectSort():
    A = [4,5,7,2,3,1,9]
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[i]>A[j]:
                A[i],A[j] = A[j],A[i]
    print(A)
    
selectSort()        