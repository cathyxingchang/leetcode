#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 49_M
# Created by xc 19/03/2017

"""
    49. Group Anagrams
    把所有的元素进行分组
    # 方法一: 96 / 100 test cases passed.
    Time Limit Exceeded 时间超时了,所以需要更换策略
"""

# 方法1
import copy
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        for index in range(0, len(strs)):
            tmpstr = strs[index]
            tmpstr_list = list(tmpstr)
            sort_str = sorted(tmpstr_list)
            # 遍历当前的result列表
            find = False
            for i in range(0, len(result)):
                if sorted(list(result[i][0])) == sort_str:
                    find = True
                    result[i].append(copy.deepcopy(tmpstr))
                    break
            if not find:
                # 增加新的分类
                result.append([])
                result[-1].append(copy.deepcopy(tmpstr))
        return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print s.groupAnagrams(strs)
