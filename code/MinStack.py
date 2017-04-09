#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 155
# Created by xc 13/03/2017

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            #  这里的边界条件很关键!!!!
            self.min_stack.append(x)
        elif x >= self.min_stack[-1]:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: voida
        """
        if not self.is_empty():
            del self.stack[-1]
            del self.min_stack[-1]

    def top(self):
        """
        :rtype: int
        """
        if not self.is_empty():
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.is_empty():
            return self.min_stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()