class Solution_20200225(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0
        for index in range(0, len(haystack)):
            if len(haystack) - index < len(needle):
                return -1
            find = 1
            for cur in range(0,len(needle)):
                if haystack[index+cur] != needle[cur]:
                    find = 0
                    break
            if find == 1:
                return index
        # 没有找到
        return -1


solution = Solution_20200225()
haystack = "aaaaaaa"
needle = "aaaa"
result = solution.strStr(haystack, needle)
print(result)