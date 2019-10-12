class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        # 最终位置分为奇数和偶数

        # 最终位置为奇数：奇数位置的元素权重为0，偶数位置的为1;
        # 最终位置为偶数：偶数位置的元素权重为0，奇数位置的为1;
        sum_odd = 0
        sum_even = 0
        for item in chips:
            if item % 2 == 0:
                sum_odd += 1
            else:
                sum_even += 1
        return min(sum_even, sum_odd)


s = Solution()
chips1 = [2,2,2,3,3]
chips2 = [1,2,3]
result = s.minCostToMoveChips(chips1)
print(result)



