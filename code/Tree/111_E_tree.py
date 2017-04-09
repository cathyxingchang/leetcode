#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 111_E_tree
# Created by xc 19/03/2017

"""
    找到树的最短长度,对树进行遍历,对叶子结点所在的层更新最短的高度.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.min_depth = None

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.process(root, 1)
        return self.min_depth

    def process(self, root, height):
        # 当前root结点所处的层数
        if root.left is None and root.right is None:
            if self.min_depth is None:
                self.min_depth = height
            if height < self.min_depth:
                self.min_depth = height
            return
        if root.left is not None:
            self.process(root.left, height + 1)
        if root.right is not None:
            self.process(root.right, height + 1)
