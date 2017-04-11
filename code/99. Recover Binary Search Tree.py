#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 99. Recover Binary Search Tree
# Created by xc 10/04/2017

import copy
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.wrong1 = None
        self.wrong2 = None
        self.last_visit = None
        self.change_state = 0

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # 下面的代码处理不了只有两个结点的情况


        if root is None:
            pass

        # 中序遍历
        self.process(root.left)

        if self.last_visit is None:
            self.last_visit = root

        elif root.val < self.last_visit.val:
            # 出现了错误
            if self.wrong1 is None:
                # 刚出现第一个错误点,也就是一个大数换到前面来了
                self.wrong1 = self.last_visit
                # 为了防止相邻数字的交换 把 wrong2也赋值
                self.wrong2 = root
            else:
                # 第一个错误已经找到了,这里是一个小数换到后面来了
                # 获取之前遍历的结点
                self.wrong2 = root
                # 交换
                tmp = self.wrong1.val
                self.wrong1.val = self.wrong2.val
                self.wrong2.val = tmp
                self.change_state = 1
        else:
            pass
        self.last_visit = root
        self.process(root.right)

        if self.change_state == 0:
            tmp = self.wrong1.val
            self.wrong1.val = self.wrong2.val
            self.wrong2.val = tmp
            self.change_state = 1



    def process(self, root):
        """
        树的中序遍历
        :param root: 
        :return: 
        """
        if root is None:
            return
        if self.change_state == 1:
            return
        self.process(root.left)
        if self.last_visit is None:
            self.last_visit = root

        elif root.val < self.last_visit.val:
            # 出现了错误
            if self.wrong1 is None:
                # 刚出现第一个错误点,也就是一个大数换到前面来了
                self.wrong1 = self.last_visit
                # 为了防止相邻数字的交换 把 wrong2也赋值
                self.wrong2 = root
            else:
                # 第一个错误已经找到了,这里是一个小数换到后面来了
                # 获取之前遍历的结点
                self.wrong2 = root
                # 交换
                tmp = self.wrong1.val
                self.wrong1.val = self.wrong2.val
                self.wrong2.val = tmp
                self.change_state = 1
        else:
            pass

        self.last_visit = root

        self.process(root.right)

root = TreeNode(3)
p = TreeNode(1)
q = TreeNode(2)
root.left = p
root.right = q
test = Solution()
test.recoverTree(root)

print root.val
