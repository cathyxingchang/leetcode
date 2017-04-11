#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 71. Simplify Path
# Created by xc 10/04/2017

"""
    简化路径
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split('/')
        path_stack = []
        for item in path_list:
            if item == '..':
                if len(path_stack) != 0:
                    path_stack.pop()
            elif item == '.' or item == '':
                pass
            else:
                path_stack.append(item)

        # 合并结果字符串
        result_path = ''
        if len(path_stack) == 0:
            result_path = '/'
            return result_path
        result_path = '/'
        for index in range(0, len(path_stack) - 1):
            result_path += path_stack[index] + '/'
        result_path += path_stack[-1]
        return result_path
# path = "/home/"
#path = "/a/./b/../../c/"
#path = '/'
#path = ''

# 错误的点
path = '/.'
path = '/..'
path = "/home/../../.."
path = '/.....'
test = Solution()
print test.simplifyPath(path)