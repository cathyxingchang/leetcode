#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 526
# Created by xc 26/02/2017

"""


class Solution(object):
    def countArrangement(self, N):


    def permutation(self, list):
        result = []
        if len(list) == 0:
            return
        for item in list:
            tmp_list = list.remove(item)
            all_tmp_list = self.permutation(tmp_list)
            for j in all_tmp_list:
                j.insert(0, item)
                result.append(j)
        return result
"""

import copy
def permutation(list1):
    '''

    :param list1:
    :return:
    '''
    result = []
    if len(list1) == 1:
        return [list1]
    for item in list1:
        tmp_list = copy.deepcopy(list1)
        tmp_list.remove(item)
        all_tmp_list = permutation(tmp_list)
        print all_tmp_list
        for j in all_tmp_list:
            j.insert(0, item)
            result.append(j)
    return result


list1 = [1, 3, 5]

result = permutation(list1)
for i in result:
    print i
