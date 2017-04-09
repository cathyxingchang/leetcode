#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wangyi_1
# Created by xc 25/03/2017

import sys
for line in sys.stdin:
    str = line.split()
    a = str[0]
    result = int(a[0])
    for index in range(1, len(a),2):
        fuhao = a[index]
        cur_num = int(a[index+1])
        if fuhao == '+':
            result += cur_num
        elif fuhao == '-':
            result -= cur_num
        elif fuhao == '*':
            result *= cur_num
        else:
            pass
print result
