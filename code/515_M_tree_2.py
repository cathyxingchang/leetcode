# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    思路:
    层次遍历
    和512_2 的思路是一致的,存储每一层最大的元素值,并继续向下遍历
"""
class Solution(object):
    def __init__(self):
        self.max_list = []

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        self.process(stack)
        return self.max_list

    def process(self, stack):
        new_stack = []
        current_max = stack[0].val
        for item in stack:
            if item.left is not None:
                new_stack.append(item.left)
            if item.right is not None:
                new_stack.append(item.right)
            if item.val > current_max:
                current_max = item.val
        self.max_list.append(current_max)
        if new_stack:
            self.process(new_stack)




