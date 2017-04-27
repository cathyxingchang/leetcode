#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 235. Lowest Common Ancestor of a Binary Search Tree(E)
# Created by xc 27/04/2017

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        lca_point = root
        if p.val < q.val:
            lp = p
            rp = q
        else:
            rp = p
            lp = q

        while lca_point is not None:
            if lp.val == lca_point.val or rp.val == lca_point.val:
                return lca_point.val
            if lp.val < lca_point.val < rp.val:
                # 已经是公共的祖先了
                return lca_point.val
            if lp.val < lca_point.val and rp.val < lca_point.val:
                # 两个结点都小于它
                lca_point = lca_point.left
            if lp.val > lca_point.val and rp.val > lca_point.val:
                lca_point = lca_point.right
        return lca_point

