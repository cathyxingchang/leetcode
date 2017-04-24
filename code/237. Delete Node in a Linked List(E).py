#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 237. Delete Node in a Linked List(E)
# Created by xc 24/04/2017
"""
    删除结点,只知道这个结点
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        val = node.next.val
        node.val = val
        node.next = node.next.next