#!/usr/bin/env python
# -*- coding: utf-8 -*-

# megcup_dog_new_2
# Created by xc 26/03/2017
import random
import copy
import math


class megcup_dog_new_2:

    def calculatexing(self, item, position):
        # print 'aaa',len(position)
        # print item
        # print position
        # 计算每个点和item的距离
        distance_list = []
        for mm in range(0, len(position)):
            print len(position)
            x1 = (item[0] - position[mm][0]) * (item[0] - position[mm][0])
            x2 = (item[1] - position[mm][1]) * (item[1] - position[mm][1])
            distance = math.sqrt(x1 + x2)
            distance_list.append((distance, position[mm][2]))
        # 对distance_list 排序
        q = sorted(distance_list)
        return q[28][1]
        pass

    def __init__(self):
        f = open("dogfood_input.txt")  # 返回一个文件对象
        line = f.readline()  # 调用文件的 readline()方法
        self.rate = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        position = []
        while line:
            # print line,  # 后面跟 ',' 将忽略换行符
            # print(line, end = '')　　　# 在 Python 3中使用
            line = f.readline()
            line = line.strip('\n')
            b = line.split(" ")
            position.append(copy.deepcopy(b))

        f.close()
        print position[0]
        del position[-1]

        # position 转int
        for index in range(0, len(position)):
            for j in range(0, len(position[0])):
                position[index][j] = int(position[index][j])
                # print position[-1]
                # print len(position)

        # 单独计算少了一行的
        loss_point = []
        for kk in range(0, 10000):
            loss_point.append([kk, 10000])
        for kk in range(0, 10000):
            loss_point.append([10000, kk])
        loss_point.append([10000, 10000])
        for item in loss_point:
            # 计算距离item 第k近的点的口味
            # print "xing",item
            kouwei = self.calculatexing(item, position)
            # 这一点的概率是1 其他点的概率是0
            self.rate[kouwei] += 1

        # 最后计算出平均值
        old_rate = [0.0, 12892371, 7724346, 11649906, 6976153, 4725919, 5328434, 8894057, 3191015, 23097966, 15519833]
        tmpxin = 0
        for index in range(0,len(old_rate)):
            tmpxin += old_rate[index]
        print "old_rate", old_rate, tmpxin

        for index in range(0, len(old_rate)):
            self.rate[index] += old_rate[index]

        sum = 0
        final_result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for index in range(0, len(self.rate)):
            sum += self.rate[index]
        print '综述',sum
        for index in range(0, len(self.rate)):
            final_result[index] = float(self.rate[index])/float(sum)
        print final_result


s = megcup_dog_new_2()