class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        result = []
        sort_arr = sorted(arr)
        min_abs = sort_arr[1] - sort_arr[0]
        for index in range(1, len(sort_arr)):
            if sort_arr[index]- sort_arr[index-1] < min_abs:
                min_abs = sort_arr[index]- sort_arr[index-1]

        for index in range(1, len(sort_arr)):
            if sort_arr[index]- sort_arr[index-1] == min_abs:
                result.append([sort_arr[index-1], sort_arr[index]])
        return result




arr = [3,8,-10,23,19,-4,-14,27]
s = Solution()
print(s.minimumAbsDifference(arr))