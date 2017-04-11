#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 94. Binary Tree Inorder Traversal
# Created by xc 10/04/2017

"""
    二叉树中序遍历
    左根右
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

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return self.result
        self.process(root.left)
        self.result.append(root.val)
        self.process(root.right)
        return self.result

    def process(self, root):
        if root is None:
            return
        self.process(root.left)
        self.result.append(root.val)
        self.process(root.right)

