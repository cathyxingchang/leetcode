#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 109_M_Convert Sorted List to Binary Search Tree
# Created by xc 29/03/2017

import copy
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.root = None

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # 首先,把head 转成list
        nums = []
        p = head
        while p is not None:
            nums.append(p.val)
            p = p.next
        self.nums = copy.deepcopy(nums)
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        begin = 0
        end = len(nums) - 1
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

nums = [1, 2, 3]
test = Solution()
test.sortedListToBST(nums)
