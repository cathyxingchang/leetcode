#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2_M
# Created by xc 28/03/2017

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        jinwei = 0
        head = None
        p3 = None
        while p1 is not None and p2 is not None:
            tmp_result = p1.val + p2.val + jinwei
            if tmp_result >= 10:
                jinwei = 1
            else:
                jinwei = 0
            tmp_node = ListNode(tmp_result % 10)
            if head is None:
                head = tmp_node
                p3 = head
            else:
                p3.next = tmp_node
                p3 = p3.next
            p1 = p1.next
            p2 = p2.next

        # 如果有还未结束的
        while p1 is not None:
            tmp_result = p1.val + jinwei
            if tmp_result >= 10:
                jinwei = 1
            else:
                jinwei = 0
            tmp_node = ListNode(tmp_result % 10)
            if head is None:
                head = tmp_node
                p3 = head
            else:
                p3.next = tmp_node
                p3 = p3.next
            p1 = p1.next

        while p2 is not None:
            tmp_result = p2.val + jinwei
            if tmp_result >= 10:
                jinwei = 1
            else:
                jinwei = 0
            tmp_node = ListNode(tmp_result % 10)
            if head is None:
                head = tmp_node
                p3 = head
            else:
                p3.next = tmp_node
                p3 = p3.next
            p2 = p2.next

        # 这里特别要注意了 最后还剩下一个
        if jinwei == 1:
            tmp_node = ListNode(1)
            if head is None:
                head = tmp_node
            else:
                p3.next = tmp_node

        return head
