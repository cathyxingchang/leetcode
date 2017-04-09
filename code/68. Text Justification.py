#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 68. Text Justification
# Created by xc 09/04/2017
"""
    字符串的格式化,每一行尽量排布更多的字符
    并且符合平铺的
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        word_stack = []
        tmp_length = 0
        index = 0
        while index < len(words):
            if len(word_stack) == 0 or tmp_length + len(words[index]) + (len(word_stack)) <= maxWidth:
                # 当前长度加上间隔的至少一个的空格长度小于最大长度,则放置一个字符串进来
                tmp_length += len(words[index])
                word_stack.append(words[index])
                index += 1
            else:
                # 当前行已经超过了最大长度,下一个放不进去了,那么把当前的存入结果中
                count = len(word_stack) - 1
                if count != 0:
                    space = (maxWidth-tmp_length) / count
                    lose_space = (maxWidth - tmp_length) - space * count
                    for i in range(0, len(word_stack)-1):
                        if i == 0:
                            result.append(word_stack[i])
                        else:
                            result[-1] += word_stack[i]
                        for j in range(0, space):
                            result[-1] += ' '
                        if lose_space != 0:
                            result[-1] += ' '
                            lose_space -= 1
                    # stack里的最后一个字符不补0
                    result[-1] += word_stack[-1]
                else:
                    # 一个字符串,后面直接加空格
                    lose_space = maxWidth - len(word_stack[0])
                    result.append(word_stack[0])
                    for i in range(0, lose_space):
                        result[-1] += ' '
                # 清空 word_stack
                word_stack = []
                tmp_length = 0
        # 最后可能stack中还有没有用完的元素 也就是最后一行
        if len(word_stack) != 0:
            if len(word_stack) > 1:
                for i in range(0, len(word_stack) - 1):
                    if i == 0:
                        result.append(word_stack[i])
                    else:
                        result[-1] += word_stack[i]
                    result[-1] += ' '
                result[-1] += word_stack[-1]
            if len(word_stack) == 1:
                result.append(word_stack[-1])
            # 补0
            lose_space = maxWidth - len(result[-1])
            for i in range(0, lose_space):
                result[-1] += ' '
        return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
#words = ["What","must","be","shall","be."]
#words = [""]
words = ["My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."]
maxWidth = 20
test = Solution()
print test.fullJustify(words, maxWidth)

