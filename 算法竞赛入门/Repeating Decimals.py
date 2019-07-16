#!/usr/bin/env python
# encoding: utf-8
'''
@author: PC-CONFIG
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: marudong951@gmail.com
@software: PC-CONFIG
@file: Repeating Decimals.py
@time: 2019/7/16 21:50
@desc:习题3-8  循环小数
'''

def main():
    a = int(input('请输入a:'))
    b = int(input('请输入b:'))

    begin = s = 0
    merc = int(a / b)   #商
    divid = a      #被除数
    rema = a % b   #余数
    remas = {}
    remas[rema] = 0
    res = str(merc)+'.'
    while True:
        begin += 1
        divid = rema*10
        merc = int(divid/b)
        rema = divid%b
        res += str(merc)
        if rema in remas:
            s = remas[rema]
            break
        else: remas[rema] = begin
    print(res,begin,s)

if __name__ == '__main__':
    main()