"""
    easy 常规问题
"""
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for item in nums:

            if len(str(item)) % 2 == 0:
                count += 1
        return count


nums = [12,345,2,6,7896]
s = Solution()
print(s.findNumbers(nums))