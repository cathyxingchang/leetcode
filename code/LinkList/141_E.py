#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 141_E
# Created by xc 15/03/2017

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    判断链表是否成环,把访问过的元素的地址放进一个数组里,
    之后进来一个新元素,都来判断是否跟之前的相连
"""
"""
    方法一 :不能通过几个比较大的测试点,时间复杂度太大了
    14/16个测试点
    存在疑问 ,is None 和 == None 的区别
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_list = []
        p = head
        if p == None:
            return False
        while True:
            if p == None:   # 这个条件有用吗? 感觉下面就已经剔除了啊 如果p.next == None 都不进行了,为什么会结果不一样呢?
                return False
            if p.next == None:
                return False
            if p.next in node_list:
                # 和之前已经遍历过的元素成环
                return True
            node_list.append(p)
            p = p.next

"""
    优化: 方法二:
    把node_list = [] 换成hasp 也就是 map
    13/16
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_list = {}
        p = head
        if p is None:
            return False
        while True:
            if p is None:   # 这个条件有用吗? 感觉下面就已经剔除了啊 如果p.next == None 都不进行了,为什么会结果不一样呢?
                return False
            if p.next is None:
                return False
            if p.next in node_list.keys():
                # 和之前已经遍历过的元素成环
                return True
            node_list[p] = 1
            p = p.next
"""
    方法三:
    网上的思路,说是一个快指针,一个慢指针,如果有环,早晚要他俩相遇的一天
    瞬间过了所有的测试点
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            # while 条件主要是为了处理无环的情况的
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False