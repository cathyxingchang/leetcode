# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
    思路:
    层次遍历法,把每次访问过得层数存下来
    重点: 特别注意第一个return!一定要认真的写好
"""

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [root]
        return self.process(stack)

    def process(self, stack):
        # new_stack 存储下一次要遍历的stack
        new_stack = []
        for i in range(0, len(stack)):
            t = stack[i]
            if t.left is not None:
                new_stack.append(t.left)
            if t.right is not None:
                new_stack.append(t.right)
        if new_stack:
            return self.process(new_stack)      # 这里的return 第一次给写丢了,一定要注意各个情况下 递归的返回情况
        else:
            # new_stack 为空,说明最左元素是stack里面最左面的那个
            return stack[0].val
