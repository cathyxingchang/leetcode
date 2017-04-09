# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    题目要求:判断两棵树是否相同
    解法: 递归
    先序遍历,看两棵子树是否一样

    其他的思路: 前序和中序,查看两个生成的串是否一样
"""


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val == q.val:
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        return False

