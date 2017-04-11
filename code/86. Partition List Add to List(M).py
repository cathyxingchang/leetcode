# -*- coding: utf-8 -*-

# 86. Partition List Add to List(M)
# Created by xc 11/04/2017
"""
    链表中元素的处理
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 变量p用来遍历
        if head is None:
            return head
        p = head
        # m 保存p之前的位置,q保存p之后的位置
        m = p
        p = p.next
        while p is not None:
            if p.val < x:
                q = p.next  # 保存p后面的位置
                begin = head
                before = None
                while begin != p:
                    if begin.val > p.val and begin.val >= x:
                        # 找到了插入的位置 并不插入头结点
                        if before is not None:
                            before.next = p
                            p.next = begin
                            m.next = q
                            p = q
                        else:
                            # 插入位置是头结点
                            p.next = begin
                            head = p
                            m.next = q
                            p = q
                        break
                    else:
                        before = begin
                        begin = begin.next
                # 如果插入的位置是队尾,相当于是并没有插入
                if begin == p:
                    m = p
                    p = p.next
                pass
            else:
                m = p
                p = p.next
        return head

head = ListNode(1)
node = [ListNode(4), ListNode(3), ListNode(2), ListNode(5), ListNode(2)]
p = head
for index in range(0,5):
    p.next = node[index]
    p = p.next

"""
head = ListNode(2)
node = [ListNode(1)]
p = head
for index in range(0, 1):
    p.next = node[index]
    p = p.next
"""
test = Solution()
result_head = test.partition(head, 3)
p = result_head
while p is not None:
    print p.val
    p = p.next
