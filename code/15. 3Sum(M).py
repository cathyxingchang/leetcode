class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sort_num = sorted(nums)
        print(sort_num)

        # 存储已经计算过的开头数字
        pass_num_set = set()
        unique_str_set = set()

        for index in range(0, len(sort_num)):
            num = sort_num[index]
            if num not in pass_num_set:
                pass_num_set.add(num)
                begin = index+1
                end = len(sort_num) - 1
                while begin < end:
                    if sort_num[begin] + sort_num[end] == 0 - num:
                        unique_str_set.add(str(num) + "_" + str(sort_num[begin]) + "_" + str(sort_num[end]))
                        begin += 1
                        end -= 1
                    elif sort_num[begin] + sort_num[end] > 0 - num:
                        end -=1
                    else:
                        begin +=1
        result = []
        for unique_str in unique_str_set:
            result.append(unique_str.split("_"))
        return result

# 要注意的情况是这种，这种情况就可能出现多个[-1,0,1]的情况，
# 为了避免这个情况，每个数字最多保留2个，0可以保留三个； 或者使用字典记录所有的数字组合
nums = [-1,-1,-1,-1]
s = Solution()
result = s.threeSum(nums)

print(result)