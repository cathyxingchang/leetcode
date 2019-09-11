# 移除括号
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # 前提条件是一定是合法的字符串，可以忽略很多异常情况
        # 存开头的下标
        index_list = []
        count = 0
        for index in range(0, len(S)):
            if count == 0:
                index_list.append(index)
                index_list.append(index-1)
            if S[index] == '(':
                count += 1
            else:
                count -= 1
        index_list.append(len(S)-1)
        result_str = ''
        for index in range(0, len(S)):
            if index not in index_list:
                result_str += S[index]
        return result_str


s = Solution()
str1 = '(()())(())(()(()))'
str2 = "(()())(())"
print(s.removeOuterParentheses(str2))