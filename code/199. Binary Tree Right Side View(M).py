#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 199. Binary Tree Right Side View(M)
# Created by xc 18/04/2017
"""
    层次遍历,每次只保留当前层的最右面的点,从右面向左面,层次遍历
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        queue = [[copy.deepcopy(root), 1]]
        while len(queue) != 0:
            top = queue[0]
            layer = top[1]
            if layer == len(result) + 1:
                # 当前层还没有元素进入
                result.append(top[0].val)
            if top[0].right is not None:
                queue.append([copy.deepcopy(top[0].right), top[1]+1])
            if top[0].left is not None:
                queue.append([copy.deepcopy(top[0].left), top[1]+1])
            # 删除对头元素
            queue.pop(0)

        # 输出结果
        return result



