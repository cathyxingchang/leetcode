class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        # pattern模式替换为数字
        pattern_num_list = []
        pattern_dict = {}
        index = 0
        for item in pattern:
            if item not in pattern_dict.keys():
                pattern_dict[item] = index
                index += 1
            pattern_num_list.append(pattern_dict[item])

        # words替换成数字
        result = []
        for word in words:
            if len(word) != len(pattern):
                continue
            words_num_list = []
            words_dict = {}
            index = 0
            flag = 1
            for i in range(len(word)):
                item = word[i]
                if item not in words_dict.keys():
                    words_dict[item] = index
                    index += 1
                words_num_list.append(words_dict[item])
                if len(words_num_list) > len(pattern_num_list) or words_num_list[i] != pattern_num_list[i]:
                    flag = 0
                    break
            if flag == 1:
                result.append(word)
        return result

s = Solution()
print(s.findAndReplacePattern(["abb","acc",""],"688"))




