#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 108_M_Convert Sorted Array to Binary Search Tree
# Created by xc 29/03/2017

#  Definition for a binary tree node.

import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.root = None
        self.nums = []

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = copy.deepcopy(nums)
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        begin = 0
        end = len(nums) -1
        mid = (begin + end) / 2
        self.root = TreeNode(nums[mid])
        # 分别生成左右子树
        self.generateTree(begin, mid - 1, self.root)
        self.generateTree(mid + 1, end, self.root)
        return self.root

    def generateTree(self, begin, end, root):
        if begin > end:
            return
        mid = (begin + end) / 2
        if self.nums[mid] < root.val:
            root.left = TreeNode(self.nums[mid])
            root = root.left
            self.generateTree(begin, mid - 1, root)
            self.generateTree(mid + 1, end, root)
        else:
            root.right = TreeNode(self.nums[mid])
            root = root.right
            self.generateTree(begin, mid - 1, root)
            self.generateTree(mid + 1, end, root)


nums = [1,2,3]
test = Solution()
test.sortedArrayToBST(nums)
