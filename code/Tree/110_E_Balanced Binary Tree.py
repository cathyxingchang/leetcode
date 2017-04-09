#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 110_E_Balanced Binary Tree
# Created by xc 30/03/2017

"""
    题目要求:判断一棵树是否是平衡二叉树
    平衡二叉树,任意一个节点的两棵子树的高度差都<=1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if self.checkBalanced(root.left) and self.checkBalanced(root.right) and abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
            return True
        else:
            return False

    def checkBalanced(self, root):
        """
        检验以root为根结点的两棵树的高度是不是一样
        :param root:
        :return:
        """
        if root is None:
            return True
        if self.checkBalanced(root.left) and self.checkBalanced(root.right) and abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
            return True
        else:
            return False


    def getHeight(self, root):
        """
        获取以root为结点的树的高度
        :param root:
        :return:
        """
        if root is None:
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1