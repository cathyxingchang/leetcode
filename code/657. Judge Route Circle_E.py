#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 657. Judge Route Circle_E
# Created by xc 14/11/2017

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        left = 0
        right = 0
        up = 0
        down = 0
        for item in moves:
            if item == 'U':
                up += 1
            elif item == 'D':
                down += 1
            elif item == 'L':
                left += 1
            else:
                right += 1
        if left == right and up == down:
            return True
        return False
