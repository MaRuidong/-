# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:05:02 2019

@author: PC-CONFIG
"""

#归并排序
def merge(A,p,q,r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    i = j = 0
    L.append(float('inf'))
    R.append(float('inf'))
    
    for k in range(p,r+1):
        if L[i]<R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1

def mergeSort(A,p,r):
    if p < r:
        q = (p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

def sort():
    A = [2,4,7,1,0,6,9,3,4,11]
    mergeSort(A,0,len(A)-1)
    print(A)

sort()