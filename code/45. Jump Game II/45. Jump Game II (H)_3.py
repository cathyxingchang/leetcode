#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 45. Jump Game II (H)_3
# Created by xc 20/04/2017
"""
    最后一个测试点不过,说明复杂度还是太大了
    动态规划竟然不好用
    http://www.cnblogs.com/ganganloveu/p/3761715.html
    参考了网上的思路:
    
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 当前的总的步数
        total_step = 0

        # 经过total_step所能到达的距离
        current_reach = 0

        # 从0~i中能到达的最大范围
        max_distance = 0

        for i in range(0, len(nums)):
            if current_reach >= len(nums) - 1:
                break
            if i > current_reach:
                total_step += 1
                current_reach = max_distance
            max_distance = max(max_distance, nums[i] + i)
        return total_step


