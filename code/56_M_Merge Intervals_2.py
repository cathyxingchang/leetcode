#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 56_M_Merge Intervals
# Created by xc 28/03/2017

"""
    之前的合并条件没有想清楚
    [1,3],[2,6]
    [1,4],[2,3]
    合并情况分为这两种
    都是a.end >= b.start 但是end 谁大取谁

    不不不 又错了
    [1,10],[2,3],[4,5],[6,7],[8,9]
    这里 10>2 end = 10 下一次比较 之前的算法是 3和4比较 但是是错误的 应该是10和4比较 应该是 current_end 来和下一个比较

    用了自己的冒泡排序算法,时间不过测试点.
    换了多维度的list排序

"""
from operator import itemgetter, attrgetter
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
        #for i in range(0, len(sorted_intervals)):
        #    for j in range(i + 1, len(sorted_intervals)):
        #        if sorted_intervals[i].start > sorted_intervals[j].start:
        #            tmp = copy.deepcopy(sorted_intervals[i])
        #            sorted_intervals[i] = copy.deepcopy(sorted_intervals[j])
        #            sorted_intervals[j] = copy.deepcopy(tmp)
        #        elif sorted_intervals[i].start == sorted_intervals[j].start:
        #            if sorted_intervals[i].end > sorted_intervals[j].end:
        #                tmp = copy.deepcopy(sorted_intervals[i])
        #                sorted_intervals[i] = copy.deepcopy(sorted_intervals[j])
        #                sorted_intervals[j] = copy.deepcopy(tmp)
        # 自己的排序算法可能效率低下 更换内置排序
        sorted_intervals = sorted(intervals, key=lambda a: (a.start, a.end))

        #for item in sorted_intervals:
        #    print item.start,item.end
        result = []
        index = 0
        while index < len(sorted_intervals):
            current_begin = sorted_intervals[index].start
            current_end = sorted_intervals[index].end
            while index + 1 < len(sorted_intervals) and current_end >= sorted_intervals[index + 1].start:
                # 修正 取当前最大的end
                current_end = max(current_end, sorted_intervals[index + 1].end)
                index += 1
            # 这一句是错误的current_end = sorted_intervals[index].end
            # 把current_begin,current_end 放入list里
            result.append(copy.deepcopy(Interval(current_begin, current_end)))
            index += 1
        for i in result:
            print "haha",i.start, i.end
        return result
intervals = [Interval(2, 7), Interval(2, 6), Interval(1, 3), Interval(8,10), Interval(15, 18)]
#intervals = [Interval(1, 4), Interval(2, 3)]
#intervals = [Interval(1, 10), Interval(4, 5), Interval(6, 7), Interval(8,9)]
test = Solution()
test.merge(intervals)