#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 82. Remove Duplicates from Sorted List II
# Created by xc 10/04/2017
"""
    这个题目比较简单的思路就是,把list转成数组,这样是不是删除起来就很方便啊
    特别注意有关数组迭代器的问题
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        new_list = []
        dictionary = {}
        index = 0
        while p is not None:
            if p.val in dictionary:
                dictionary[p.val]['count'] += 1
            else:
                dictionary[p.val] = {
                    'count': 1,
                    'index': index
                }
            index += 1
            p = p.next
        # 对字典中的index进行排序
        sorted_dictionary = sorted(dictionary.iteritems(), key=lambda x: x[1]['index'])
        head = None
        #for key in sorted_dictionary:
        # 这里注意,字典是用排序迭代器进行排序的,所以输出是turple类型的元素了
        # [(1, {'count': 1, 'index': 2}), (2, {'count': 3, 'index': 7})]
        for item in sorted_dictionary:
            if item[1]['count'] == 1:
                if head is None:
                    head = ListNode(item[0])
                    p = head
                else:
                    new_node = ListNode(item[0])
                    p.next = new_node
                    p = p.next
        return head

