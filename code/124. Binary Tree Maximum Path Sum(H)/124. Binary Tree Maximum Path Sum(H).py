#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 124. Binary Tree Maximum Path Sum(H)
# Created by xc 17/04/2017

"""
    二叉树的最大路径长度
    
    最大路径长度只可能有三种情况
    1:全在左子树上
    2:全在右子树上
    3:跨越了左子树和右子树
    
    陷阱: 里面可能有小于0的数字
    那么取max的时候,就不能取0了
    
    这道题看似容易,其实不愧为一道hard题! 需要考虑的边界条件很多,还有需要考虑时间复杂度的问题
    91 / 92 test cases passed.
    有一个长测试点不过
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        length1 = None
        length2 = None

        # 1:全在左子树上
        if root.left is not None:
            length1 = self.maxPathSum(root.left)
        # 2:全在右子树上
        if root.right is not None:
            length2 = self.maxPathSum(root.right)
        # 3:跨越了左子树和右子树,需要左子树的最大路径长度和右面的
        # 左右子树是可以为0的,如果小于0的话,可以根本不要这条路
        length3 = root.val + max(self.max_path(root.left), 0) + max(self.max_path(root.right), 0)

        # 要注意避免路径长度小于0的情况
        # [-3] 这种情况左右子树的长度为0 但是这样就不包含结点了
        # length 3 肯定没有问题,一定会包含结点,但是length1和length2就不一定了
        pool = []
        if length1 is not None:
            pool.append(length1)
        if length2 is not None:
            pool.append(length2)
        pool.append(length3)
        return max(pool)

    def max_path(self, root):
        """
        以root为根节点的树的最大的路径长度
        :param root: 
        :return: 
        """
        if root is None:
            return 0
        left_path = self.max_path(root.left)
        right_path = self.max_path(root.right)
        # 这里也是同样的道理,如果左右子树为0的话,是可以不取的
        return max(left_path, right_path, 0) + root.val

