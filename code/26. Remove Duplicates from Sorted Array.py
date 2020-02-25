class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # 因为已经是排好序的，所以只要后面的数字和前面的不相同，就可以+1
        """
        if len(nums) <= 1:
            return nums

        current_num = nums[0]
        index = 1
        while index < len(nums):
            if nums[index] == current_num:
                nums.pop(index)
            else:
                current_num = nums[index]
                index += 1



nums = [0,1,1,1,2,3,4,5]
nums = [1,1]
solution = Solution()
solution.removeDuplicates(nums)
print(nums)
