"""
    最长回文子串=找出所有的回文子串里最长哪一个
    dp[i][j]表示从i到j是否为回文串
    dp[i][j] 和 dp[i+1][][j-1] 之间的关系
"""


class Solution_20200121(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        max_length = 1
        max_str = s[0]
        dp = [[0 for i in range(0, len(s))] for j in range(0,len(s))]
        for i in range(0, len(s)):
            dp[i][i] = 1
        for i in range(len(s), -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and (dp[i + 1][j - 1] == 1 or i+1 > j-1 ):
                    dp[i][j] = 1
                    if j-i+1 > max_length:
                        max_length = j-i+1
                        max_str = s[i:j+1]
        # print(dp)
        return max_str

s = Solution_20200121()
print(s.longestPalindrome(""))
