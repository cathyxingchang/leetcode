#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 217_E
# Created by xc 09/03/2017

"""
 查找数组中是否有重复元素
 不是直接用异或运算 是不对的
"""
# 这个算法不知道为什么超时了,很奇怪 按理来说 应该是O(n)的复杂度,不应该啊
# ???? d
# 思路1:不通过
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 当nums只有0个元素和1个元素时,也符合
        dict = {}
        for index in range(0,len(nums)):
            if nums[index] in dict.keys():
                # 有重复元素
                return True
            else:
                dict[nums[index]] = 1
        return False



# 思路2:可通过
"""
    这个就过了???没道理啊??只是因为最后一个大数据的原因吗? 还是为什么呢?
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 没必要考虑只有0和1的情况能和下面合并,只要考虑了就好了
        if len(nums) == 0 or len(nums) == 1:
            return False
        sorted_nums = sorted(nums)
        for index in range(1, len(nums)):
            if sorted_nums[index] == sorted_nums[index-1]:
                # 有重复元素
                return True
        return False
