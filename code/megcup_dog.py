#!/usr/bin/env python
# -*- coding: utf-8 -*-

# megcup_dog
# Created by xc 26/03/2017
import random
import copy
import math


def calculatexing(item, position):
    #print 'aaa',len(position)
    #print item
    #print position
    # 计算每个点和item的距离
    distance_list = []
    for mm in range(0, len(position)):
        x1 = (item[0]-position[mm][0])*(item[0]-position[mm][0])
        x2 = (item[1]-position[mm][1])*(item[1]-position[mm][1])
        distance = math.sqrt(x1 + x2)
        distance_list.append((distance, position[mm][2]))
    # 对distance_list 排序
    q = sorted(distance_list)
    return q[28][1]
    pass


f = open("dogfood_input.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法

position = []
while line:
    #print line,  # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()
    line = line.strip('\n')
    b = line.split(" ")
    position.append(copy.deepcopy(b))

f.close()

del position[-1]


# position 转int
for index in range(0, len(position)):
    for j in range(0, len(position[0])):
        position[index][j] = int(position[index][j])
#print position[-1]
#print len(position)

# 随机生成10个点
all_points = []
for i in range(0, 10000):
       generateddata = [random.randint(0, 10000), random.randint(0, 10000)]
       if not generateddata in all_points:  #去掉重复数据
               all_points.append(generateddata)

print "随机完毕"
rate = []

for item in all_points:
    # 计算距离item 第k近的点的口味
    #print "xing",item
    kouwei = calculatexing(item, position)
    # 这一点的概率是1 其他点的概率是0
    tmp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 11个0 方便运算
    tmp[kouwei] = 1
    rate.append(copy.deepcopy(tmp))


# rate = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# 计算平均值
sum_kouwei = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for index in range(0, len(rate)):
    for j in range(0, len(rate[0])):
        sum_kouwei[j] += rate[index][j]


result_rate = []
for index in range(0, len(sum_kouwei)):
    result_rate.append(sum_kouwei[index]/float(len(all_points)))

print "bada", result_rate
