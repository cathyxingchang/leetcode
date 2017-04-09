# -*- coding: utf-8 -*-

# 144_M_tree_2
# Created by xc 20/03/2017

"""
    二叉树的遍历:
    题目要求非递归,所以练习一个递归和非递归吧
    这里是非递归算法
    非递归的方法使用堆栈进行处理
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return []
        stack = []
        p = root
        while len(stack) > 0 or p is not None:
            while p is not None:
                # 访问栈顶元素
                result.append(p.val)
                # 继续访问下一层的元素
                stack.append(p)
                p = p.left
            # 已经把左面这一路走完了,退栈
            p = stack[-1]
            stack.pop()
            p = p.right
        return result

