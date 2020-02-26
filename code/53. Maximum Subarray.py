class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 需要单独考虑的是，如果全是负数的话，那么最小的那个是最大值
        if len(nums) == 0:
            return 0
        max_num = max(nums)
        if max_num < 0:
            return max(nums)

        max_sum = 0
        current_sum = 0
        for item in nums:
            current_sum += item
            if current_sum > max_sum:
                max_sum = current_sum
            elif current_sum < 0:
                current_sum = 0
        return max_sum


solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
# 全是负数
nums = [-1,-2]
# 全是0
nums = [0,0]
result = solution.maxSubArray(nums)
print(result)