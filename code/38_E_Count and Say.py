#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 38_E_Count and Say
# Created by xc 28/03/2017
import copy
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        last_list = [1]
        for turns in range(2, n + 1):
            index = 0
            new_last_list = []
            while index < len(last_list):
                current_count = 1
                current_num = last_list[index]
                while index + 1 < len(last_list) and last_list[index] == last_list[index + 1]:
                    current_count += 1
                    index += 1
                index += 1
                # 统计完一组
                new_last_list.append(current_count)
                new_last_list.append(current_num)
            turns += 1
            last_list = copy.deepcopy(new_last_list)
        # 拼接
        result = ""
        for item in last_list:
            result += str(item)
        #print type(result)
        return result

test = Solution()
print test.countAndSay(1)



