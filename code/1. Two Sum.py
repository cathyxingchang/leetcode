"""

    two sum问题
    简单排序问题
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_pair = []
        for index in range(0, len(nums)):
            nums_pair.append([nums[index], index])
        # 排序
        nums_pair.sort(key=lambda x: (x[0]))

        begin = 0
        end = len(nums)-1
        while begin < end:
            if nums_pair[begin][0] + nums_pair[end][0] == target:
                return [nums_pair[begin][1], nums_pair[end][1]]
            elif nums_pair[begin][0] + nums_pair[end][0] > target:
                end -= 1
            else:
                begin += 1


s = Solution()
nums = [7,2]
target = 9
print(s.twoSum(nums,target))


