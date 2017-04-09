#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 226_E_tree
# Created by xc 26/02/2017

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    题目要求:交换两棵树的子树
    思路:交换根节点->交换左子树,交换右子树
"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
