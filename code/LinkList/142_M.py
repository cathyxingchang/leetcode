#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 142_M
# Created by xc 18/03/2017

"""
    1   2   3   4   5   6   7   8   9   10->4

    slow    1   2   3   4   5   6   7   8
    fast    1   3   5   7   9   4   6   8

    1   2   3   4   5   6   7   8   9   10->1

    slow    1   2   3   4   5   6   7   8   9  10   1   在拐过弯的地方相遇
    fast    1   3   5   7   9   1   3   5   7   9   1

    不对,好像并不是会出现在开头

    1   2   3   4   5   6   7   8   9 ->1
    slow    1   2   3   4   5   6   7   8   9   1
    fast    1   3   5   7   9   2   4   6   8   1

    1   2   3   4   5   6   7   8   9 ->2
    slow    1   2   3   4   5   6   7   8   9
    fast    1   3   5   7   9   3   5   7   9

    规律是错误的 详细信息请参考印象笔记

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            # while 条件主要是为了处理无环的情况的
            slow_before = slow
            fast_before = fast.next
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet = slow
                p = head
                q= meet
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None
