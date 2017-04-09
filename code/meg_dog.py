#!/usr/bin/env python
# -*- coding: utf-8 -*-

# meg_dog
# Created by xc 26/03/2017

qq = 0
for block_row in range(0, 100):
    print qq
    for block_col in range(0, 100):
        # 每一层块 生成100*100个点
        begin_row = block_row * 100
        begin_col = block_col * 100
        for i in range(begin_row, begin_row + 100, 1):
            for j in range(begin_col, begin_col + 100, 1):
                # 生成100个点
                qq += 1

print qq
for kk in range(0, 10001):
    qq += 1
    qq += 1


qq -= 1

print 100001*100001
print 'haha',qq
