class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 如果只有一个元素
        if head.next is None:
            return None
        p = head
        q = head
        before = None
        for i in range(0, n):
            q = q.next
        # 如果删除的是第一个元素
        if q is None:
            head = head.next
            return head

        while q:
            before = p
            p = p.next
            q = q.next

        before.next = p.next
        return head

# 测试点：
# 删除第一个元素； 删除最后一个元素；
head1 = ListNode(1)
n12 = ListNode(2)
n13 = ListNode(3)
n14 = ListNode(4)
head1.next = n12
n12.next = n13
n13.next = n14

# 只有一个元素
head2 = ListNode(1)

head3 = ListNode(1)
n32 = ListNode(2)
head3.next = n32


solution = Solution()
result = solution.removeNthFromEnd(None, 2)
while result:
    print(result.val)
    result = result.next
