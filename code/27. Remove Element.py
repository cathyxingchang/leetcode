class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

solution = Solution()

nums = [3,2,2,3]
val = 3

nums = [1,1]
val = 1

nums = [1,9,2,1]
val = 1
solution.removeElement(nums,val)
print(nums)