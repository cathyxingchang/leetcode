class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        # 一个字母只能用一次
        chars_dict = {}
        for item in chars:
            if item in chars_dict.keys():
                chars_dict[item] += 1
            else:
                chars_dict[item] = 1
        total = 0
        print(chars_dict)

        for word in words:
            flag = 1
            word_dict = {}
            for item in word:
                if item not in chars_dict.keys():
                    flag = 0
                    break
                if item in word_dict.keys():
                    word_dict[item] += 1
                    if word_dict[item] > chars_dict[item]:
                        flag = 0
                        break
                else:
                    word_dict[item] = 1
            total += flag * len(word)
        return total

s=Solution()
print(s.countCharacters(["cat","bt","hat","tree"],'atach'))