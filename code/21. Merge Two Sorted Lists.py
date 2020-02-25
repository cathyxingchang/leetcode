
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_20200220(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            head = ListNode(l2.val)
            l2 = l2.next
        else:
            head = ListNode(l1.val)
            l1 = l1.next

        p = head
        while l1 and l2:
            if l1.val > l2.val:
                q = ListNode(l2.val)
                l2 = l2.next
            else:
                q = ListNode(l1.val)
                l1 = l1.next
            p.next = q
            p = p.next

        while l1:
            q = ListNode(l1.val)
            p.next = q
            l1 = l1.next
            p = p.next
        while l2:
            q = ListNode(l2.val)
            p.next = q
            l2 = l2.next
            p = p.next

        return head


l1 = ListNode(1)
l11 = ListNode(3)
l12 = ListNode(4)
l1.next = l11
l11.next = l12


l2 = ListNode(5)
l21 = ListNode(6)
l22 = ListNode(9)
l2.next = l21
l21.next = l22


solution = Solution_20200220()
result = solution.mergeTwoLists(l1,l2)
while result:
    print(result.val)
    result = result.next