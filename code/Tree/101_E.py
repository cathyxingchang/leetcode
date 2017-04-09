#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 101_E
# Created by xc 19/03/2017
"""
    判断一棵树是不是二叉镜像树
    大概是这样的? 最开始,把一棵树拆成最优两个子树,然后同时进行
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.process(root.left, root.right)

    def process(self, left_tree, right_tree):
        # 这个函数判断 left_tree和right_tree是否是镜像的
        # 1.判断是否为空
        if left_tree is None and right_tree is None:
            return True
        if left_tree is None:
            return False
        if right_tree is None:
            return False

        # 2.判断当前结点是否相同
        if left_tree.val != right_tree.val:
            return False
        return self.process(left_tree.left, right_tree.right) and self.process(left_tree.right, right_tree.left)
