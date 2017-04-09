#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 223_M
# Created by xc 13/03/2017

"""
    计算矩形所覆盖的所有的面积
    点给的都是左下角和右上角
    思路是,计算两个矩形的面积然后减去两个矩形之间的面积
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # 计算两个矩形的面积
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)

        # 计算重叠区域的面积
        height = min(D, H) - max(B, F)
        width = min(C, G) - max(A, E)
        if height > 0 and width > 0:
            area3 = height * width
        else:
            area3 = 0
        return area1 + area2 - area3
