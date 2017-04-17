#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 144. Binary Tree Preorder Traversal(M)
# Created by xc 17/04/2017
"""
    二叉树遍历:
    非递归:
    中序遍历
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import copy
class Solution(object):
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return self.result
        p = root
        stack = [copy.deepcopy(p)]
        self.result.append(p.val)
        p = p.left
        while not (p is None and len(stack) == 0):
            while p is not None:
                stack.append(copy.deepcopy(p))
                self.result.append(p.val)
                p = p.left
            p = stack[-1]
            stack.pop()
            p = p.right
        return self.result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
test = Solution()
print test.preorderTraversal(root)
