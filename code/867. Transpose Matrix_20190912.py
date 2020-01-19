# 转置数组
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        row = len(A)
        col = len(A[0])
        for i in range(0, col):
            tmp = []
            for j in range(0, row):
                tmp.append(A[j][i])
            result.append(tmp)
        return result

A = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print(s.transpose(A))


