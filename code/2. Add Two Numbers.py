# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_20190121(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        jinwei = 0
        l3 = None
        p = None
        while l1 and l2:
            total = l1.val+l2.val+jinwei
            q = ListNode(total % 10)
            if l3 is None:
                l3 = q
                p = l3
            else:
                p.next = q
                p = p.next
            jinwei = int(total / 10)
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                total = l1.val + jinwei
                q = ListNode(total % 10)
                if l3 is None:
                    l3 = p
                else:
                    p.next = q
                    p = p.next
                jinwei = int(total / 10)
                l1 = l1.next
            pass
        elif l2:
            while l2:
                total = l2.val + jinwei
                q = ListNode(total % 10)
                if l3 is None:
                    l3 = p
                else:
                    p.next = q
                    p = p.next
                jinwei = int(total / 10)
                l2 = l2.next
        if jinwei != 0:
            q = ListNode(jinwei)
            p.next = q
            p = p.next

        return l3


l1 = ListNode(9)
l11 = ListNode(9)
l12 = ListNode(9)
l1.next = l11
l11.next = l12

l2 = ListNode(9)
l21 = ListNode(9)
l22 = ListNode(9)
l2.next = l21
l21.next = l22

s = Solution_20190121()
result = s.addTwoNumbers(l1,l2)
while result:
    print(result.val)
    result = result.next
print(result)

