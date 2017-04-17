#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 150. Evaluate Reverse Polish Notation(M)
# Created by xc 16/04/2017
"""
。也就是c语言中，除法是向零取整，即舍弃小数点后的数。而在python中，
  是向下取整的。而这道题的oj是默认的c语言中的语法，所以需要在遇到'/'的时候注意一下。
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = 0
        num = []
        for item in tokens:
            if item == '+' or item == '-' or item == '*' or item == '/':
                if item == '+':
                    tmp_result = num[-2] + num[-1]
                elif item == '-':
                    tmp_result = num[-2] - num[-1]
                elif item == '*':
                    tmp_result = num[-2] * num[-1]
                else:
                    if num[-2] * num[-1] < 0:
                        tmp_result = -((-num[-2]) / num[-1])
                    else:
                        tmp_result = num[-2] / num[-1]
                num.pop()
                num[-1] = tmp_result
            else:
                num.append(int(item))
        return num[-1]

tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#tokens = ["-1","-2","+"]
test = Solution()
print test.evalRPN(tokens)

a = 10
b = -132
c = a/b
print c