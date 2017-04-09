#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 21_E
# Created by xc 16/03/2017

"""
    合并两个有序的链表
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        if p1 is None:
            return l2
        if p2 is None:
            return l1
        # 决定头结点
        if p1.val < p2.val:
            l3 = p1
            p1 = p1.next
        else:
            l3 = p2
            p2 = p2.next
        p3 = l3
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
            else:
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
        if p1 is not None:
            p3.next = p1
            return l3
        if p2 is not None:
            p3.next = p2
            return l3
