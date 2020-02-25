class Solution20200218(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        边界值考虑欠妥，numRow*2-2=0 没有考虑
        """
        # 数组的长度
        result = ""
        # 处理边界值
        if numRows == 1:
            return s
        numList = ["" for i in range(0, numRows)]
        for index in range(0, len(s)):
            tmp = index % (numRows*2-2)
            if tmp < numRows:
                numList[tmp] += s[index]
            else:
                numList[numRows*2-2-tmp] += s[index]
        for i in range(0, numRows):
            result += numList[i]
        return result


s = ""
numRows = 3
solution = Solution20200218()
print(solution.convert(s, numRows))
print("PAHNAPLSIIGYIR")