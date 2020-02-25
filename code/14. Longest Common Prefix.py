class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_len = len(strs[0])
        for str in strs:
            min_len = min(min_len, len(str))
        if min_len == 0:
            return ""

        prefix = ""
        for location in range(0, min_len):
            compare_str = strs[0][location]
            for str in strs:
                if str[location] != compare_str:
                    return prefix
            prefix += compare_str

        return prefix

solution = Solution()
strs = ["  1","  11","  111"]
print(solution.longestCommonPrefix(strs))