#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 124. Binary Tree Maximum Path Sum(H)
# Created by xc 17/04/2017

"""
    二叉树的最大路径长度
    
    最大路径长度只可能有三种情况
    1:全在左子树上
    2:全在右子树上
    3:跨越了左子树和右子树
    
    陷阱: 里面可能有小于0的数字
    那么取max的时候,就不能取0了
    
    这道题看似容易,其实不愧为一道hard题! 需要考虑的边界条件很多,还有需要考虑时间复杂度的问题
    91 / 92 test cases passed.
    有一个长测试点不过
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_length = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.max_length = root.val
        self.max_path(root)
        return self.max_length

    def max_path(self, root):
        """
        以root为根节点的树的最大的(或左或右的)路径长度
        :param root: 
        :return: 
        """
        if root is None:
            return 0

        length1 = self.max_path(root.left)
        length2 = self.max_path(root.right)
        # 跨越了左子树和右子树,需要左子树的最大路径长度和右面的
        # 左右子树是可以为0的,如果小于0的话,可以根本不要这条路
        length3 = root.val + max(length1, 0) + max(length2, 0)
        if length3 > self.max_length:
            self.max_length = length3
        current_path = max(max(length1, 0), max(length2, 0)) + root.val
        return current_path


