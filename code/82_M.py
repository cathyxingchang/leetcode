#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 82_M
# Created by xc 21/03/2017

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        new_head = head
        p = new_head
        q = new_head.next
        while q is not None:
            if p.val != duplicate_num:
                p.next = q
                p = p.next
                duplicate_num = p.val
            else:
                q = q.next

