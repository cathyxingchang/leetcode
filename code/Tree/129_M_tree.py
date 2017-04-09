#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 129_M
# Created by xc 15/03/2017

"""
    一道树的问题,计算每个叶子节点上面的路径的和
    思路1:1 直接遍历,遇到叶子结点,就把上面的结果加和
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.total_sum = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.process(root, root.val)
        return self.total_sum

    def process(self, root, sum):
        """
        这个函数记录到了root这个结点的时候,当前的和 sum是包括root的
        需要保证 root 一直都不为空
        :param root: 当前的根结点
        :param sum: 当前的和
        :return:
        """
        if root.left is not None:
            self.process(root.left, sum * 10 + root.left.val)
        if root.right is not None:
            self.process(root.right, sum * 10 + root.right.val)
        if root.left is None and root.right is None:
            # root是叶子结点
            self.total_sum += sum


