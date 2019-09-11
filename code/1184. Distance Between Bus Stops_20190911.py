class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        # 计算正向的front
        front = 0
        back = 0
        if destination < start:
            tmp = destination
            destination = start
            start = tmp

        for index in range(start, destination):
            front += distance[index]

        # 计算反向的
        for index in range(destination, len(distance)):
            back += distance[index]

        for index in range(0, start):
            back += distance[index]
        return min(front, back)

s = Solution()
distance = [7,10,1,12,11,14,5,0]

start = 7
destination = 2
result = s.distanceBetweenBusStops(distance, start, destination)
print(result)
