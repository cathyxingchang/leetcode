#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 56_M_Merge Intervals
# Created by xc 28/03/2017

"""
    [[1,4],[2,3]] 这是错误的,情况考虑不够周全
    这一版本是错误的,正确的在下一版本
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import copy
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # 首先,intervals进行排序
        # 冒泡排序
        sorted_intervals = copy.deepcopy(intervals)
        for i in range(0, len(sorted_intervals)):
            for j in range(i + 1, len(sorted_intervals)):
                if sorted_intervals[i].start > sorted_intervals[j].start:
                    tmp = copy.deepcopy(sorted_intervals[i])
                    sorted_intervals[i] = copy.deepcopy(sorted_intervals[j])
                    sorted_intervals[j] = copy.deepcopy(tmp)
                elif sorted_intervals[i].start == sorted_intervals[j].start:
                    if sorted_intervals[i].end > sorted_intervals[j].end:
                        tmp = copy.deepcopy(sorted_intervals[i])
                        sorted_intervals[i] = copy.deepcopy(sorted_intervals[j])
                        sorted_intervals[j] = copy.deepcopy(tmp)
        result = []
        index = 0
        while index < len(sorted_intervals):
            current_begin = sorted_intervals[index].start
            while index + 1 < len(sorted_intervals) and sorted_intervals[index].end >= sorted_intervals[index + 1].start:
                index += 1
            current_end = sorted_intervals[index].end
            # 把current_begin,current_end 放入list里
            result.append(copy.deepcopy(Interval(current_begin, current_end)))
            index += 1
        #for i in result:
        #    print "haha",i.start, i.end
        return result
intervals = [Interval(2, 7), Interval(2, 6), Interval(1, 3), Interval(8,10), Interval(15, 18)]
test = Solution()
test.merge(intervals)