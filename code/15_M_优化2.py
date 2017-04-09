#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 15_M_优化2
# Created by xc 22/03/2017

"""
    3Sum问题:
    排序后转化为2sum问题
    现在的去重复策略是用字典保存,但是只能是在保存的时候帮助去重,在运行计算过程中,并不会有很多优势
    所以策略改变,每个相同的元素最多保存2个(只有0可以保存3个,其实干脆都保存3个吧,省事),这样就可以有效的简化运算过程了
    Runtime: 1622 ms
    啊 好像并没有被优化,速度更慢了.....
    可能应该是边删除元素边排序??
"""
import time

class Solution(object):
    def __init__(self):
        # 为了方便剔除重复的元素,使用字典进行保存
        self.dic = {}
        self.result = []

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        # 排序后转成2sum问题
        nums.sort()

        # 优化策略:
        current_num = nums[0]
        frequency = 1
        index = 1
        length = len(nums)
        while index < length:
            if nums[index] == current_num:
                # 重复数字
                frequency += 1
                if frequency > 3:
                    del nums[index]
                    length -= 1     # 这里很关键!数组的长度也随之改变了
                else:
                    index += 1
            else:
                # 非重复数字
                current_num = nums[index]
                frequency = 1
                index += 1
        print nums
        # 可以排除一部分重复的数据 但是第一次运算这个数据的时候,后面大量的重复数据还是有冗余的
        before_num = None
        for index in range(0, len(nums)-2):
            # 把3sum问题转化为2sum问题
            if before_num is None:
                before_num = nums[index]
                self.twoSum(nums[index+1:], nums[index]*(-1))
            else:
                if before_num == nums[index]:
                    # 重复数据不做处理
                    continue
                else:
                    self.twoSum(nums[index + 1:], nums[index] * (-1))

        for key in self.dic:
            num_set = [key[0], key[1], key[2]]
            self.result.append(num_set)
        return self.result

    def twoSum(self, nums, target):
        begin = 0
        end = len(nums)-1
        while begin < end:
            if nums[begin]+nums[end] == target:
                key = (-1 * target, nums[begin], nums[end])
                self.dic[key] = 1
                # 还需要找下一组和符合的
                end -= 1
                begin += 1
            elif nums[begin]+nums[end] > target:
                end -= 1
                pass
            else:
                begin += 1

nums = [-1,0,1,2,-1,-4]

start = time.clock()
s = Solution()
print s.threeSum(nums)
end = time.clock()
total_time = (end - start)*1000
print "运行时间: %f ms" % total_time