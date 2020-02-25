class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]

        # 无斜率 是纵轴
        if x2 - x1 == 0:
            for item in coordinates:
                if item[0] != x2:
                    return False
            return True

        # y=kx+b
        # python 计算的时候会自动转换小数
        k = (y2-y1)/(x2-x1)
        b = y1-k*x1
        for item in coordinates:
            if k*item[0] + b != item[1]:
                return False
        return True

