#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 76. Minimum Window Substring
# Created by xc 09/04/2017
"""
    收获是要善于自己写测试点
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 首先为t构建字典,存储每个元素的位置
        t_diction = {}
        for letter in t:
            if letter not in t_diction:
                t_diction[letter] = {
                    'location': [],
                    'count': 1
                }
            else:
                t_diction[letter]['count'] += 1
        full = 0
        begin = -1
        end = -1
        min_length = len(s)+1
        min_begin = 0
        min_end = 0
        for index in range(0, len(s)):
            letter = s[index]
            if letter not in t_diction:
                continue
            if letter in t_diction and t_diction[letter]['count'] > len(t_diction[letter]['location']):
                # t串当前位置的元素还没有被填满
                t_diction[letter]['location'].append(index)
                if begin == -1:
                    begin = index
                end = index
            else:
                # t串当前元素已经满了,判定是否要向前了
                # 判断当前字典是否已经被最大填满
                if full != 1:
                    # 计算是否已经填满full
                    for item in t_diction:
                        if t_diction[item]['count'] != len(t_diction[item]['location']):
                            full = 0
                            break
                        full = 1
                if full == 1:
                    # 已经填满 首先计算当前的长度
                    current_len = end - begin + 1
                    if current_len < min_length:
                        min_length = current_len
                        min_begin = begin
                        min_end = end
                # 替换字典中当前元素的最小位置
                t_diction[letter]['location'].sort()
                if t_diction[letter]['location'][0] == begin:
                    # 被替换掉的是begin,更新begins
                    # 遍历字典,保存第二大的
                    t_diction[letter]['location'][0] = index
                    new_min_index = len(s)
                    for item in t_diction:
                        if len(t_diction[item]['location']) != 0:
                            tmp_min = min(t_diction[item]['location'])
                        else:
                            tmp_min = len(s)+1
                        if tmp_min < new_min_index:
                            new_min_index = tmp_min
                    begin = new_min_index
                t_diction[letter]['location'][0] = index
                end = index
        # 晕乎乎的,最后的"长度"和最后的"覆盖状态"是无法确定的
        # 计算覆盖状态
        if full != 1:
            # 计算是否已经填满full
            for item in t_diction:
                if t_diction[item]['count'] != len(t_diction[item]['location']):
                    full = 0
                    break
                full = 1
        if full == 1:
            current_len = end - begin + 1
            if current_len < min_length:
                min_length = current_len
                min_begin = begin
                min_end = end
        # 没有完整的包括整个数组
        if full == 0:
            return ""
        return s[min_begin: min_end + 1]




s = "ADOBECODEBANC"
t = "ABC"
s = "AAAAABAAACAAAAA"
t = "ABC"
s = ""
t = "ABC"
# 最后这个测试点检验出了自己的问题
s = "AABBCD"
t = "BCD"
test = Solution()
print test.minWindow(s,t)








