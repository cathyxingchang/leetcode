#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 144_M
# Created by xc 20/03/2017

"""
    二叉树的遍历:
    题目要求非递归,所以练习一个递归和非递归吧
    这里是递归算法
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.process(root)
        return self.result

    def process(self, root):
        if root is None:
            return
        self.result.append(root.val)
        self.process(root.left)
        self.process(root.right)