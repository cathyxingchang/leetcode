class Solution20200218(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        蓄水问题
        蓄水量: abs(height[i] - height[j])*(j-i)
        """
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


solution = Solution20200218()
height = [2,9]
result = solution.maxArea(height)
print(result)
