#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 15. 3Sum
# Created by yangchao 27/03/2017
import time
class Solution(object):
    def __init__(self):
        self.mat = []

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.mat = nums
        l = len(nums)
        self.quickSort(0, l-1)
        #self.mat.sort()
        first_set = []
        print self.mat
        for i in range(0, l):
            if self.mat[i] in first_set:
                continue
            second_set = []
            first_set.append(self.mat[i])
            begin = i + 1
            end = l - 1
            q = - self.mat[i]
            while begin < end:
                p = self.mat[begin] + self.mat[end]
                if p == q:
                    if self.mat[begin] in second_set:
                        end -= 1
                        continue
                    second_set.append(self.mat[begin])
                    result.append([self.mat[i], self.mat[begin], self.mat[end]])
                    begin += 1
                    end -= 1
                elif p > q:
                    end -= 1
                else:
                    begin += 1
        return result

    def quickSort(self, b, e):
        if e-b < 1:
            return
        key = self.mat[b]
        begin = b
        end = e
        while e > b:
            if self.mat[e] >= key:
                e -= 1
                continue
            if self.mat[b] <= key:
                b += 1
                continue
            self.mat[e], self.mat[b] = self.mat[b], self.mat[e]
        self.mat[begin], self.mat[b] = self.mat[b], self.mat[begin]

        if b - begin > 1:
            self.quickSort(begin, b-1)
        if end - b > 1:
            self.quickSort(b+1, end)





s = Solution()





print(s.threeSum([-1,0,1,2,-1,-4]))
# [[-1,-1,2],[-1,0,1]]
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# [-1, 0, 1],[-1, -1, 2]
print(s.threeSum([-1, 2, -1, -3, 1, -1, 2]))
# [-1, 2, -1],[2, -3, 1]
print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
# [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
print(s.threeSum([-5,1,-3,-1,-4,-2,4,-1,-1]))
# [[-5,1,4],[-3,-1,4]]

