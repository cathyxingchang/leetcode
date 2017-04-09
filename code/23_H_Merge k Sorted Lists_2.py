#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 23_H_Merge k Sorted Lists
# Created by xc 29/03/2017
"""
    策略:每次放置进每个链表的后续数字,选取当前情况下最小的
    128 / 130 test cases passed.

    修正后,通过测试样例
"""
import copy
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 结果的指针和head
        result_list = None
        result_p = result_list

        # 获取链表的个数
        length = len(lists)

        if length == 0:
            return []
        # 为每个链表构建一个指针
        p = [head for head in lists]
        end_count = 0
        tmp = []
        # 获取当前链表里面最大的
        for index in range(0, length):
            if p[index] is None:
                end_count += 1
                continue
            else:
                tmp.append(p[index])
        tmp = sorted(tmp, key=lambda p: p.val)
        while end_count < length:
            # 获取最小值
            q = tmp[0]
            # 放置在新的链表中
            if result_list is None:
                result_list = q
                result_p = result_list
            else:
                result_p.next = q
                result_p = result_p.next
            # 把最小位置的元素删除出去
            del tmp[0]
            q = q.next
            if q is not None:
                begin = 0
                end = len(tmp)-1
                position = None
                while begin <= end:
                    mid = (begin + end) / 2
                    if tmp[mid].val == q.val:
                        position = mid
                        break
                    elif tmp[mid].val > q.val:
                        end = mid - 1
                    else:
                        begin = mid + 1
                if position is None:
                    if begin == -1:
                        position = 0
                    else:
                        position = begin
                tmp.insert(position, q)
            else:
                # 有一个空了
                end_count += 1
        # 现在只剩下一个空的了 同时tmp里也只有一个元素了
        if len(tmp) == 1:
            result_p.next = tmp[0]
        return result_list



a = None
b = ListNode(6)
c = ListNode(2)
test = Solution()
print test.mergeKLists([a])
