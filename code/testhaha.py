#!/usr/bin/env python
# -*- coding: utf-8 -*-

# testhaha
# Created by xc 02/04/2017

import numpy
nlist=[52,48,48,51,52,49,48,52]
N= 8
narray=numpy.array(nlist)
sum1=narray.sum()
narray2=narray*narray
sum2=narray2.sum()
mean=sum1/N
var=sum2/N-mean**2
print var