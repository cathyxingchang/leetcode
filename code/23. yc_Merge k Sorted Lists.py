#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 23. Merge k Sorted Lists
# Created by yangchao 28/03/2017
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.result = None
        self.saved = ListNode(0)

    def generateNode(self, val):
        if self.result is None:
            self.result = ListNode(val)
            self.saved.next = self.result
        else:
            self.result.next = ListNode(val)
            self.result = self.result.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)
        while 1:
            min_num = None
            exist_num = 0
            min_nodes = []
            for i in range(0, l):
                item = lists[i]
                if item is not None:
                    exist_num += 1
                    if min_num is None or item.val < min_num:
                        min_num = item.val
                        min_nodes = [i]
                    elif item.val == min_num:
                            min_nodes.append(i)
            if exist_num < 1:
                return self.saved.next
            if exist_num == 1:
                last_one = lists[min_nodes[0]]
                while last_one is not None:
                    self.generateNode(last_one.val)
                    last_one = last_one.next
                return self.saved.next
            for i in min_nodes:
                self.generateNode(lists[i].val)
                lists[i] = lists[i].next

l1 = ListNode(1)
head1 = l1
l1.next = ListNode(2)
l1 = l1.next
l1.next = ListNode(3)
l1 = l1.next
l1.next = ListNode(4)
l1 = l1.next
l1.next = ListNode(5)
l1 = l1.next

l2 = ListNode(6)
head2 = l2
l2.next = ListNode(7)
l2 = l2.next
l2.next = ListNode(8)
l2 = l2.next
l2.next = ListNode(9)
l2 = l2.next
l2.next = ListNode(10)
l2 = l2.next

s = Solution()
r = s.mergeKLists([head1, head2])
while r is not None:
    print r.val, '->'
    r = r.next

