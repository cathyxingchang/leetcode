class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 获取每一行每一列的最大值
        max_row_length = []
        for line in grid:
            max_row_length.append(max(line))
        max_col_length = []
        for col in range(0, len(grid)):
            nums = []
            for row in range(0, len(grid)):
                nums.append(grid[row][col])
            max_col_length.append(max(nums))

        # 遍历数组，找到所在行列的最大值，取两个值中的较小值
        count = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid)):
                final = min(max_row_length[row], max_col_length[col])
                count += final - grid[row][col]
        return count



s = Solution()
grid = [[3,0,8,4],
        [2,4,5,7],
        [9,2,6,3],
        [0, 3, 1, 0]]
print(s.maxIncreaseKeepingSkyline(grid))