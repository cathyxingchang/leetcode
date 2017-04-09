#!/usr/bin/env python
# -*- coding: utf-8 -*-

# problemB
# Created by xc 05/03/2017

import sys
import string
import os



def is_letter(char):
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        return True
    else:
        return False


def is_match(str1, str2):
    index1 = 0
    index2 = 0
    flag0 = False
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    #print 'diu'
    if len(str1) == 0 and len(str2) == 0:
        return True
    if len(str1) == 0 or len(str2) == 0:
        return False
    while index1 < len(str1) and index2 < len(str2):
        if is_letter(str1[index1]) and is_letter(str2[index2]) and str1[index1] == str2[index2]:
            index1 += 1
            index2 += 1
        elif is_letter(str1[index1]) and is_letter(str2[index2]) and str1[index1] != str2[index2]:
            return False
        elif str1[index1] == '*':
            # 额外的一种情况,* 是最后一个字母了
            if index1 == len(str1)-1:
                if index2 + 3 >= len(str2):
                    return True
            flag0 = is_match(str1[index1 + 1:], str2[index2:])
            if flag0:
                return True
            if index2 + 1 < len(str2):
                flag1 = is_match(str1[index1 + 1:], str2[index2+1:])
                if flag1:
                    return True
            if index2 + 2 < len(str2):
                flag2 = is_match(str1[index1 + 1:], str2[index2+2:])
                if flag2:
                    return True
            if index2 + 3 < len(str2):
                flag3 = is_match(str1[index1 + 1:], str2[index2+3:])
                if flag3:
                    return True
            if index2 + 4 < len(str2):
                flag4 = is_match(str1[index1 + 1:], str2[index2+4:])
                if flag4:
                    return True
            return False

        elif str2[index2] == '*':
            # 额外的一种情况,* 是最后一个字母了
            if index2 == len(str2)-1:
                if index1 + 3 >= len(str1):
                    return True
            flag0 = is_match(str2[index2 + 1:], str1[index1:])
            if flag0:
                return True
            if index1 + 1 < len(str1):
                flag1 = is_match(str2[index2 + 1:], str1[index1+1:])
                if flag1:
                    return True
            if index1 + 2 < len(str1):
                flag2 = is_match(str2[index2 + 1:], str1[index1+2:])
                if flag2:
                    return True
            if index1 + 3 < len(str1):
                flag3 = is_match(str2[index2 + 1:], str1[index1+3:])
                if flag3:
                    return True
            if index1 + 4 < len(str1):
                flag4 = is_match(str2[index2 + 1:], str1[index1+4:])
                if flag4:
                    return True
            return False
    if index1 == len(str1) and index2 == len(str2):
        return True
    return False





str1 = 'Shakes*e'
str2 = 'S*speare'
str1 = 'Shakes*e'
str2 = '*peare'

file_object = './test.txt'
f = open(file_object, 'r')
w = open('./result.txt','w')
n = 50

for i in range(1, 2):
    str1 = f.readline()
    str1 = str1.strip()
    str2 = f.readline()
    str2 = str2.strip()
    #print str1,'哈哈', str2
    result = is_match(str1, str2)
    #print result
    if result:
        tmp_str = 'Case #'+str(i)+': TRUE\n'
        w.write(tmp_str)
    else:
        tmp_str = 'Case #' + str(i) + ': FALSE\n'
        w.write(tmp_str)
w.close()
