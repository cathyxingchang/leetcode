#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 404_E_tree
# Created by xc 02/03/2017

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
    思路:
    核心思路是 :遍历
    具体是:
    遍历每个元素,判断当前元素是其父结点的左结点还是右面结点,也就是把这个left还是right的flag传下去
"""


class Solution(object):
    def __init__(self):
        self.count = 0

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # flag = 1 定义为查找左子树
        # flag = 2 定义为查找右子树
        # 分别查找左右子树
        if root is None:
            return 0
        if root.left is None and root.right is None:
            # 只有一个根结点,返回0
            return 0
        self.process(root.left, 1)
        self.process(root.right, 2)
        return self.count

    def process(self, root, flag):
        if root is None:
            return
        if root.left is None and root.right is None:
            # root 是叶子结点
            if flag == 1:
                self.count += root.val
        self.process(root.left, 1)
        self.process(root.right, 2)

