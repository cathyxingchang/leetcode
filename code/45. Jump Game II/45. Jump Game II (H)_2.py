#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 45. Jump Game II (H)_2
# Created by xc 20/04/2017
"""
    之前的方法并不能处理数字全都一样的情况
    比如[1,1,1,1,1,1,1.....]
    复杂度相当于是n^2了 复杂度过高
    方法修改为,从前面往后推导,更新当前点所能到达的所有的点
    
    可是还是有问题
    逆序测试点不通过 (一步可达的大测试点)
    91 / 92 test cases passed.
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 前提是保证有路径
        # d是初始化,每个人所能到达的路径 d[i] 代表能走到第i位置的最短步数
        d = [i for i in range(0, len(nums))]
        for i in range(0, len(nums)):
            current_step = nums[i]  # 当前点所能走的最远的距离
            for step in range(1, current_step + 1):
                if i + step >= len(nums):
                    break
                if d[i] + 1 < d[i + step]:
                    # 从i直接跳过来比之前的最短步数要小
                    d[i + step] = d[i] + 1
        print d
        return d[-1]

nums = [2,3,1,1,1,4,2]
test = Solution()
print test.jump(nums)

