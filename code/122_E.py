#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 122_E
# Created by xc 20/03/2017
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        for index in range(1,len(prices)):
            total_profit += max(0, prices[index] - prices[index - 1])
        return total_profit