#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 458_E
# Created by xc 09/03/2017

"""
    如果用数目最小的猪,测出n碗里那个有毒药
    举个例子:8碗
    二进制: 1000
    0001:   0号吃
    0010:   1号吃
    0011:   0号,1号吃
    0100:   2号吃
    哪一位有数,就让那个猪吃
    最后根据猪死的位置,来还原原来的数字
    也就是说,这个数字换成二进制有几位
"""

# 这是错误的解法 不行
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # 可以检测的次数
        times = int(minutesToTest/minutesToDie)
        # 每次需要计算的篮子数
        if buckets % times == 0:
            # 如果能除开
            each_time_bucket = buckets / times
        else:
            each_time_bucket = int(buckets / times) + 1
        # 计算each_time_bucket能用多少位二进制表示
        # 多少位
        weishu = 0
        while each_time_bucket != 0:
            weishu += 1
            each_time_bucket = int(each_time_bucket / 2)
        return weishu

# 上面的解法是错误的
# http://www.cnblogs.com/mux1/p/6275797.html
# 用每一头猪,控制一个维度
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """

        # 一定要认证,需要考虑边界情况
        # 只有1个的时候,可以直接鉴别出毒药来
        if buckets == 1:
            return 0
        # 可以检测的次数,决定了一头猪可以控制几维
        times = int(minutesToTest/minutesToDie)
        weidu = times + 1
        pig_count = 1
        current_buckets = weidu
        while current_buckets < buckets:
            pig_count += 1
            current_buckets *= weidu
        return pig_count

