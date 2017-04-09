#!/usr/bin/env python
# -*- coding: utf-8 -*-

# wangyi_3
# Created by xc 25/03/2017


#coding = utf-8
import sys
import copy
if __name__ == "__main__":
    # 读取第一行的n  一共要处理的工作数
    n = int(sys.stdin.readline().strip())
    m = 2
    ans = 0
    machine_time = []
    for i in range(0,1):
        # 读取一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        # 获取每个值
        values = map(int, line.split())
        for v in values:
            machine_time.append(copy.deepcopy(v))
    # 保存当前的时间数目
    machine_list = [0, 0]
    if n == 1:
        print machine_time[0]
    if n == 2:
        # 机器数大于工作数
        print max(machine_time)
    else:
        # 首先排序
        machine_time.sort()

        print max(machine_list)
