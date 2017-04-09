#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 112_E_tree
# Created by xc 08/03/2017

"""
    题目要求:
    计算树的路径长度,判断是否存在一条路径,使得sum = 22
    思路还是递归
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    陷阱题,万一是负数呢!!!这里一定要小心
"""
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.process(root, root.val, sum)

    def process(self, root, cur_sum, target):
        """
        :param root:        当前根结点
        :param cur_sum:     到达root结点时,当前层的值
        :param target:      目标值
        :return:
        """
        ######## 特别注意,这里不对,因为万一target是负数呢
        #if cur_sum > target:
        #    # 已经大于目标值,直接返回
        #    return False
        if cur_sum == target and root.left is None and root.right is None:
            # root已经达到了叶子节点,且值符合
            return True
        if root.left is None and root.right is None:
            # 已经到了叶子结点,但是值不符合
            return False
        if root.left is None:
            return self.process(root.right, cur_sum + root.right.val, target)
        if root.right is None:
            return self.process(root.left, cur_sum + root.left.val, target)
        else:
            return self.process(root.left, cur_sum + root.left.val, target) or self.process(root.right, cur_sum + root.right.val, target)
