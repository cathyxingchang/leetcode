#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 146. LRU Cache(H)
# Created by xc 16/04/2017

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        #
        self.least)
        # 上一次访问的元素
        self.last_key = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 如果不在里面,则不返回-1,不做处理
        if key not in self.cache:
            return -1

        # 如果在里面,返回value,同时更新
        # 步骤如下:
        # 1.修改当前元素的前后
        before = self.cache[key]['before']
        after = self.cache[key]['after']
        self.cache[before]['after'] = self.cache[after]['before']

        # 2.修改最后
        self.cache[key]['before'] = self.last_key
        self.cache[self.last_key]['after'] = key

        # 3.修改最近被访问过的元素
        self.last_key = key

        return self.cache[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # 如果在里面??

        # 如果表格无空间,则放入,只更新当前结点和之前的结点

        # 如果表格无空间,则替换,同时更新



        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)