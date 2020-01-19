class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        # 是个排列组合的数学问题
        title_dict = {}
        for item in tiles:
            if item in title_dict.keys():
                title_dict[item] += 1
            else:
                title_dict[item] = 1


