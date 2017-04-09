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
    题目要求打印所有值为某个值的路径
    陷阱题,万一是负数呢!!!这里一定要小心
    又一个陷阱,如果没有元素呢,返回什么呢
    一个树的遍历问题,只要认真一点,仔细一点,应该问题不大,虽然做的慢,但是应该也没问题的
"""

import copy


class Solution(object):
    def __init__(self):
        self.final_result = []   # List[List[int]] 保存最终的结果

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return self.final_result

        cur_list = []       # List[]  保存当前的路径的list
        cur_list.append(root.val)
        self.process(root, root.val, cur_list, sum)
        return self.final_result


    def process(self, root, cur_sum, cur_list, target):
        """
            函数计算的是访问到root的时候,当前队伍的值以及list,list包含root
        :param root:        当前根结点
        :param cur_sum:     到达root结点时,当前层的值
        :param cur_list:    当前这条路径的list
        :param target:      目标值
        :return:
        """
        if cur_sum == target and root.left is None and root.right is None:
            # root已经达到了叶子节点,且值符合
            # 把当前的list放进result里
            self.final_result.append(cur_list)
            return
        if root.left is None and root.right is None:
            # 已经到了叶子结点,但是值不符合
            # 这里应该不用退栈,因为我应该是一遍遍历到底才会出现list
            return
        if root.left is None:
            new_list = copy.deepcopy(cur_list)
            new_list.append(root.right.val)
            self.process(root.right, cur_sum + root.right.val, new_list, target)
            return
        if root.right is None:
            new_list = copy.deepcopy(cur_list)
            new_list.append(root.left.val)
            self.process(root.left, cur_sum + root.left.val, new_list, target)
            return
        else:
            new_list = copy.deepcopy(cur_list)
            new_list.append(root.left.val)
            self.process(root.left, cur_sum + root.left.val, new_list, target)
            new_list = copy.deepcopy(cur_list)
            new_list.append(root.right.val)
            self.process(root.right, cur_sum + root.right.val, new_list, target)
            return
