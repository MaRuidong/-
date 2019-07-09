#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Digit Counting.py
@time: 2019/7/9 22:26
@desc:
'''

def main(s):
    tb = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for c in s:
        tb[c] += 1
    print(tb)

if __name__ == '__main__':
    s = input('请输入字符串：')
    main(s)