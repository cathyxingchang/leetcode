#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 114_MFlatten Binary Tree to Linked List
# Created by xc 30/03/2017

"""
    扁平化一棵树
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.new_tree = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            pass
        else:
            # tree的先序遍历
            self.new_tree = TreeNode(root.val)
            p = self.new_tree
            self.process(root.left, p)
            self.process(root.right, p)

            root = self.new_tree
            print 'g'

    def process(self, root, p):
        """
        :param root: 当前的结点
        :param p: 新树的根节点
        :return:
        """
        if root is None:
            return
        p.right = TreeNode(root.val)
        p = p.right
        self.process(root.left, p)
        self.process(root.right, p)

head = TreeNode(1)
a = TreeNode(2)

head.left = a

test = Solution()
m = test.flatten(head)
print m

