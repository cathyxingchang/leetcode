#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 77_M
# Created by xc 19/03/2017

import copy
class Solution(object):
    def __init__(self):
        self.result = []
        self.tmp_result = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.process(n, k)
        return self.result

    def process(self, m, k):
        # 从1到m的数里,找k个数
        # 为了方便,数组是从后面往前找的
        # 要求 m>=k
        if k == 0:
            # 这一组组合找完了
            # !!!!这里确实不能用 直接赋值 不然还是有错误的 list 经常有是指针的时候
            self.result.append(0)
            self.result[len(self.result)-1] = copy.deepcopy(self.tmp_result)
            return
        for choose in range(m, k-1, -1):
            # 把choose放进数组里
            self.tmp_result.append(choose)
            # 继续向后找
            self.process(choose-1, k-1)
            # 把choose拿出去
            self.tmp_result.pop()

s = Solution()
s.combine(4, 2)
print s.result
