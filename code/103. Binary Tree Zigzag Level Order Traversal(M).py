#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 103. Binary Tree Zigzag Level Order Traversal(M)
# Created by xc 18/04/2017

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return []
        stack = [[copy.deepcopy(root), 1]]
        tmp = []
        while len(stack) != 0:
            top = stack[0]
            layer = top[1]
            if layer == len(result) + 2:
                # 上一层已经结束了
                if (layer - 1) % 2 == 0:
                    # 上一层的是偶数层,从右面往左
                    result.append(copy.deepcopy(tmp[::-1]))
                else:
                    result.append(copy.deepcopy(tmp))
                tmp = []
            tmp.append(top[0].val)
            stack.pop(0)
            if top[0].left is not None:
                stack.append([copy.deepcopy(top[0].left), layer + 1])
            if top[0].right is not None:
                stack.append([copy.deepcopy(top[0].right), layer + 1])
        # 最后tmp中应该还有空余的元素
        if (len(result) + 1) % 2 == 0:
            # 当前层是偶数层,右到左
            result.append(copy.deepcopy(tmp[::-1]))
        else:
            result.append(copy.deepcopy(tmp))
        return result



