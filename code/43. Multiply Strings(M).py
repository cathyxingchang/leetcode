#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 43. Multiply Strings(M)
# Created by xc 12/04/2017
"""
    大数乘法
    You are here! 
    Your runtime beats 5.77% of python submissions.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 里面所有的变量都是list
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = list(num1)
        num2 = list(num2)
        final = []
        # 把num1放在第一行,用num2去计算
        zero_count = 0
        for index in range(len(num2) - 1, -1, -1):
            single_result = self.single_multiply(num1, num2[index])
            # single_result 左移,补0
            for i in range(0, zero_count):
                single_result.append('0')
            final = self.add_num(final, single_result)
            zero_count += 1
        return ''.join(final)

    def single_multiply(self,num1,single):
        """
        返回单数single和num1的乘积结果
        :param num1: 
        :param single: 
        :return: 
        """
        result = []
        jinwei = 0
        if single == '0':
            return ['0']
        if single == 1:
            return num1
        # 翻转num1
        num1 = num1[::-1]
        single = int(single)
        for i in range(0, len(num1)):
            a = int(num1[i])
            tmp_sum = single * a + jinwei
            result.append(str(tmp_sum % 10))
            jinwei = tmp_sum / 10
        if jinwei != 0:
            result.append(str(jinwei))
        result = result[::-1]
        return result



    def add_num(self, num1, num2):
        # 两个大数的加法
        # 首先颠倒两个数,然后在短的数字后面补0,之后从第一位向后加,最后再逆转
        result = []
        jinwei = 0
        n1 = num1[::-1]
        n2 = num2[::-1]
        if len(n1) > len(n2):
            for i in range(0, len(n1) - len(n2)):
                n2.append('0')
        else:
            for i in range(0, len(n2) - len(n1)):
                n1.append('0')
        if len(n1) != len(n2):
            print 'dududu'
        for i in range(0, len(n1)):
            a = int(n1[i])
            b = int(n2[i])
            tmp_sum = a+b+jinwei
            result.append(str(tmp_sum % 10))
            jinwei = tmp_sum / 10
        if jinwei == 1:
            result.append('1')
        result = result[::-1]
        return result

num1 = '0'
num2 = '0'

num1 = '0'
num2 = '50'

test = Solution()
print test.multiply(num1,num2)