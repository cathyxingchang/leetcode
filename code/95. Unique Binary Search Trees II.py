#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 95. Unique Binary Search Trees II
# Created by xc 11/04/2017
"""
    二叉树的生成
    递归生成所有的二叉树
    
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
