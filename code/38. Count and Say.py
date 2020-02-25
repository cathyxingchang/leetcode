class Solution(object):
    def countNum(self, nums):
        nums = str(nums)
        result = ""
        current_num = nums[0]
        count = 1
        for index in range(1, len(nums)):
            item = nums[index]
            if item == current_num:
                count += 1
            else:
                result += str(count) + str(current_num)
                count = 1
                current_num = item
        # 这里特别注意，如果上面的for循环结束了，那么最后一组就没有放进去
        result += str(count) + str(current_num)
        return result

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count_list = [0, 1, 11]
        if n <= 2:
            return count_list[n]

        for i in range(3, n+1):
            nums = count_list[i-1]
            cur = self.countNum(nums)
            count_list.append(cur)
        return count_list[n]


solution = Solution()
print(solution.countAndSay(5))