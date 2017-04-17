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
        self.least_recent = None
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
        if self.last_key == key:
            return self.cache[key]['value']

        # 如果在里面,返回value,同时更新
        # 步骤如下:
        # 0. 根据情况判断是否修改least_recent
        if self.capacity == 1 or len(self.cache) == 1:
            self.last_key = key
            self.least_recent = key
            return self.cache[key]['value']

        if self.least_recent == key:
            # 需要替换least_recent
            self.least_recent = self.cache[self.least_recent]['after']
            self.cache[self.least_recent]['before'] = None

        # 1.修改当前元素的前后,防止链表断开
        before = self.cache[key]['before']
        after = self.cache[key]['after']
        if before is not None and after is not None:
            self.cache[before]['after'] = after
            self.cache[after]['before'] = before
        elif before is None and after is None:
            pass
        elif before is None:
            self.cache[after]['before'] = None
        else:
            self.cache[before]['after'] = key
            pass

        # 2.修改最后
        self.cache[key]['before'] = self.last_key
        self.cache[key]['after'] = None
        self.cache[self.last_key]['after'] = key

        # 3.修改最近被访问过的元素
        self.last_key = key

        return self.cache[key]['value']

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # 如果在里面,则set值
        if key in self.cache:
            # 1.更新当前元素的value值
            self.cache[key]['value'] = value

            # 2.根据情况判断是否修改least_recent
            if len(self.cache) == 1:
                self.least_recent = key
                self.last_key = key
                return

            if self.least_recent == key:
                # 恰好访问了马上要被删除的元素
                self.least_recent = self.cache[self.least_recent]['after']

            # 把当前元素挪到最后去
            # 1.修改当前元素的前后,防止链表断开
            before = self.cache[key]['before']
            after = self.cache[key]['after']
            if before is not None and after is not None:
                self.cache[before]['after'] = after
                self.cache[after]['before'] = before
            elif before is None and after is None:
                pass
            elif before is None:
                self.cache[after]['before'] = None
            else:
                self.cache[before]['after'] = key

            # 更新新元素和之前元素的前后
            self.cache[key]['before'] = self.last_key
            self.cache[key]['after'] = None
            self.cache[self.last_key]['after'] = key
            self.last_key = key

        # 如果表格有空间,则放入,只更新当前结点和之前的结点
        elif len(self.cache) < self.capacity:
            self.cache[key] = {
                'value': None,
                'before': None,
                'after': None
            }
            self.cache[key]['value'] = value
            if self.capacity == 1:
                self.least_recent = key
                self.last_key = key
                return
            self.cache[key]['before'] = self.last_key
            if self.last_key is not None:
                self.cache[self.last_key]['after'] = key
            if self.least_recent is None:
                self.least_recent = key

            self.last_key = key

        # 如果表格无空间,则替换,同时更新
        else:
            if self.capacity == 1:
                self.cache.pop(self.least_recent)
                self.cache[key] = {
                    'value': value,
                    'before': None,
                    'after': None
                }
                self.least_recent = key
                self.last_key = key
                return
            # 替换最近未被使用的元素
            tmp = self.least_recent
            self.least_recent = self.cache[self.least_recent]['after']
            # 更新被删除元素后面值得before
            next_element = self.cache[tmp]['after']
            self.cache[next_element]['before'] = None
            # 删除least_recent元素
            self.cache.pop(tmp)
            # 放入新元素
            self.cache[key] = {
                'value': None,
                'before': None,
                'after': None
            }
            self.cache[key]['value'] = value
            # 更新新元素和之前元素的前后
            self.cache[key]['before'] = self.last_key
            self.cache[self.last_key]['after'] = key
            self.last_key = key



# Your LRUCache object will be instantiated and called as such:

capacity = 2
obj = LRUCache(capacity)
obj.put(2, 1)
print obj.least_recent
print obj.cache

obj.put(2, 2)
print obj.least_recent
print obj.cache

print obj.get(2)
print obj.least_recent
print obj.cache

obj.put(1, 1)
print obj.least_recent
print obj.cache

obj.put(4, 1)
print obj.least_recent
print obj.cache

print obj.get(2)
print obj.least_recent
print obj.cache

print obj.get(3)
print obj.least_recent
print obj.cache
"""
capacity = 2
obj = LRUCache(capacity)
obj.put(1, 1)
print obj.cache

obj.put(2, 2)
print obj.cache

param_1 = obj.get(1)
print obj.cache

obj.put(3,3)
print obj.cache

print obj.get(2)
print obj.cache

obj.put(4, 4)
print obj.cache

print obj.get(1)
print obj.cache

print obj.get(3)
print obj.cache

print obj.get(4)
print obj.cache
"""

