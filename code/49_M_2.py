#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 49_M_2
# Created by xc 20/03/2017

"""
    由于方法一中时间超时了,所以我们调整策略,调整成字典 再试试

    99 / 100 test cases passed.
    这次还是不过,就差一点了
"""
# 方法1
import copy
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        result = []
        for tmpstr in strs:
            tmpstr_list = list(tmpstr)
            tmpstr_list.sort()
            # 在字典中找
            # 这一行就不对 下一行就对,为什么??
            # if "".join(tmpstr_list) in dic.keys():
            if "".join(tmpstr_list) in dic:
                key = "".join(tmpstr_list)
                dic[key].append(tmpstr)
            else:
                key = "".join(tmpstr_list)
                dic[key] = [tmpstr]
        for key in dic:
            result.append(dic[key])
        return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print s.groupAnagrams(strs)
