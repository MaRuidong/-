# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:18:41 2019

@author: PC-CONFIG
"""

#从小到大快速排序
def quickSort():
    A = [6,4,8,9,0,3,7,2]
    
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    print("排序后 ",A)
    
quickSort()    