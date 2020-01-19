class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_count_dict = {}
        for item in arr:
            if item in arr_count_dict.keys():
                arr_count_dict[item] += 1
            else:
                arr_count_dict[item] = 1
        occurrences_set = set()
        for num in arr_count_dict:
            if arr_count_dict[num] in occurrences_set:
                return False
            else:
                occurrences_set.add(arr_count_dict[num])
        return True


s = Solution()
arr1 = [1,2,2,1,1,3]
arr2 = [1,2]
print(s.uniqueOccurrences(arr2))



