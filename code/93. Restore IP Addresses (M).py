#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 93. Restore IP Addresses (M)
# Created by xc 11/04/2017
"""
    想要简化,却发现好像没有很好的简化出来,反而因为前面自己提出的几个情况造成了边界条件的错误
"""

class Solution(object):
    def __init__(self):
        self.result_address = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        tmp_stack = []
        if len(s) <= 3:
            return []
        if len(s) == 12:
            if 100 <= int(s[0:3]) <= 255 and 100 <= int(s[3:6]) <= 255 and 100 <= int(s[6:9]) <= 255 and 100 <= int(
                    s[9:12]) <= 255:
                self.result_address = [s[0:3] + '.' + s[3:6] + '.' + s[6:9] + '.' + s[9:12]]
            return self.result_address

        tmp_stack.append(s[0])
        self.process(s[1:], tmp_stack)
        tmp_stack.pop()

        if len(s) >= 2 and int(s[0] + s[1]) >= 10:
            tmp_stack.append(s[0] + s[1])
            self.process(s[2:], tmp_stack)
            tmp_stack.pop()
        if len(s) >= 3 and 100 <= int(s[0] + s[1] + s[2]) <= 255:
            tmp_stack.append(s[0] + s[1] + s[2])
            self.process(s[3:], tmp_stack)
            tmp_stack.pop()
        return self.result_address

    def process(self, s, tmp_stack):
        if len(s) == 0 and len(tmp_stack) == 4:
            # 满足了ip地址的条件
            ip_address = tmp_stack[0] + '.' + tmp_stack[1] + '.' + tmp_stack[2] + '.' + tmp_stack[3]
            self.result_address.append(ip_address)
            return
        if len(s) > (4 - len(tmp_stack)) * 3:
            # 剩下的长度远远大于一个ip地址的长度了
            return
        if len(s) < 4 - len(tmp_stack):
            # 字符串不够生成地址的了
            return
        # 继续向下处理
        tmp_stack.append(s[0])
        self.process(s[1:], tmp_stack)
        tmp_stack.pop()

        if len(s) >= 2 and int(s[0] + s[1]) >= 10:
            tmp_stack.append(s[0] + s[1])
            self.process(s[2:], tmp_stack)
            tmp_stack.pop()
        if len(s) >= 3 and 100 <= int(s[0] + s[1] + s[2]) <= 255:
            tmp_stack.append(s[0] + s[1] + s[2])
            self.process(s[3:], tmp_stack)
            tmp_stack.pop()

string_test = "25525511135"
#string_test = "0000"
string_test = '1111'
string_test ="103574606193"
test = Solution()
print test.restoreIpAddresses(string_test)