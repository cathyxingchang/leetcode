#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 98
# Created by xc 21/03/2017

"""
    二叉搜索树是中序遍历的结果是递增的
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

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.process(root)
        for index in range(1, len(self.result)):
            if self.result[index] <= self.result[index-1]:
                return False
        return True

    def process(self, root):
        if root is None:
            return
        # 遍历左子树
        self.process(root.left)
        # 遍历当前结点
        self.result.append(root.val)
        # 遍历右子树
        self.process(root.right)
