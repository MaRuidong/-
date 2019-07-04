#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: garner
@file: fileOpe.py
@time: 2019/7/3 21:18
@desc:
'''

import os

def fileOpera(path):
    with open(path,'r',encoding='utf-8') as file:
        for line in file.readlines():
            print(line)

