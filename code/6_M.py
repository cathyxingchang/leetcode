#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 6_M
# Created by xc 27/03/2017

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 特别要注意的边界条件
        if numRows <= 1:
            return s
        # 构建一个有numRows行的数组 学到的新知识
        result = [[] for i in range(0, numRows)]
        for index in range(0, len(s)):
            set = 2 * numRows - 2
            yushu = index % set
            if yushu < numRows:
                result[yushu].append(s[index])
            else:
                result[set - yushu].append(s[index])
        # 最后的字符串都放在result的三行里
        p = [''.join(result[i]) for i in range(0, numRows)]
        # print p
        q = ''.join(p)

        yc = ''.join([''.join(result[i]) for i in range(0, numRows)])
        return yc



s = "PAYPALISHIRING"
numRows = 5
test = Solution()
print test.convert(s, numRows)