"""
    字符串里的回文子串数目
"""

class Solution(object):
    def isPalindromic(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 如果s[i..j]是回文子串，那么如果s[i-1] == s[j+1] 那么也是
        dp = [[0 for j in range(0, len(s))] for i in range(0, len(s))]
        for i in range(0, len(s)):
            dp[i][i] = 1
        # for j in range(1,len(s)):
        #     if self.isPalindromic(s, 0, j):
        #         dp[0][j] = 1
        # print(dp)

        # j>i
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and (dp[i+1][j-1] == 1 or i+1 > j-1):
                    dp[i][j] = 1
        #print(dp)
        result = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                result += dp[i][j]
        return result


solution = Solution()
s = "aaa"
print(solution.countSubstrings(s))
