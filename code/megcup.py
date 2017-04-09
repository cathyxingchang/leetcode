#!/usr/bin/env python
# -*- coding: utf-8 -*-

# megcup
# Created by xc 26/03/

import math


def distance(point1, point2):
    m = point1[0] - point2[0]
    n = point1[1] - point2[1]
    k = m*m + n*n
    return math.sqrt(k)

A = (4.7, 6.6)
B = (-4.3, -1.2)
C = (5.3, 5.5)

A = (-1, 0)
B = (5, -5)
C = (0, 2)

print distance(A,B)
print distance(A,C)