#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 102_M(107)
# Created by xc 23/03/2017


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = []
        result = []
        queue.append((root, 1))
        index = 0
        while index < len(queue):
            # 导出当前层的元素,同时把当前层所连接的子结点也放入后面的quene中
            level = queue[index][1]
            k = index
            tmp = []
            while k < len(queue) and queue[k][1] == level:
                tmp.append(queue[k][0].val)
                # 把当前结点的子结点放入quene中
                if queue[k][0].left is not None:
                    queue.append((queue[k][0].left, level + 1))
                if queue[k][0].right is not None:
                    queue.append((queue[k][0].right, level + 1))
                k += 1
            result.append(copy.deepcopy(tmp))
            # index向前移动
            index = k
        return result
