class Solution_20200219(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sort_num = sorted(nums)
        if len(nums) < 3:
            return ""
        min_value = abs(nums[0] + nums[1] + nums[2] - target)
        result = nums[0] + nums[1] + nums[2]

        # 存储已经计算过的开头数字
        pass_num_set = set()

        for index in range(0, len(sort_num)):
            num = sort_num[index]
            if num not in pass_num_set:
                pass_num_set.add(num)
                begin = index + 1
                end = len(sort_num) - 1
                while begin < end:
                    if abs(sort_num[begin] + sort_num[end] + num - target) < min_value:
                        min_value = abs(sort_num[begin] + sort_num[end] + num - target)
                        result = sort_num[begin] + sort_num[end] + num
                    if sort_num[begin] + sort_num[end] == target - num:
                        return target
                    elif sort_num[begin] + sort_num[end] > target - num:
                        end -= 1
                    else:
                        begin += 1

        return result


nums = [-1, 2, 1, -4]
target = 1
s = Solution_20200219()
result = s.threeSumClosest(nums,target)

print(result)