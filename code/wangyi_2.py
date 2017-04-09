#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wangyi_2
# Created by xc 25/03/2017

import sys
for line in sys.stdin:
    a = line.split()
    w = int(a[0])
    x = int(a[1])
    y = int(a[2])
    z = int(a[3])
    result_dic = {}
    for p in range(w, x+1):
        for q in range(y, z+1):
            result_dic[float(p)/float(q)] = 1
print len(result_dic)