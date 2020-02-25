"""
    思路 (h, k)中，h从大到小排序，从小到大排序
    特别需要注意的地方时数组为[]的情况，提交的两次报错都是这个原因
"""
import numpy as np


class Solution(object):
    def reconstructQueue_1(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(people) == 0 or len(people) == 1:
            return people
        data = np.array(people)
        index = np.lexsort([data[:, 1], -1 * data[:, 0]])
        sorted_people = data[index, :]
        # print(sorted_people)
        result = [[sorted_people[0][0], sorted_people[0][1]]]

        for index in range(1, len(sorted_people)):
            h = sorted_people[index][0]
            k = sorted_people[index][1]
            # 从前往后找位置
            higher_count = 0
            location = 0
            while higher_count < k and location < len(result):
                if result[location][0] >= h:
                    higher_count += 1
                    location += 1
                else:
                    location += 1
            if location == len(result):
                result.append([h,k])
            else:
                result.insert(location, [h,k])

            # print(index, location, result)

        return result

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) == 0 or len(people) == 1:
            return people
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))  # 关键在这一行
        result = [[sorted_people[0][0], sorted_people[0][1]]]

        for index in range(1, len(sorted_people)):
            h = sorted_people[index][0]
            k = sorted_people[index][1]
            # 从前往后找位置
            higher_count = 0
            location = 0
            while higher_count < k and location < len(result):
                if result[location][0] >= h:
                    higher_count += 1
                    location += 1
                else:
                    location += 1
            if location == len(result):
                result.append([h, k])
            else:
                result.insert(location, [h, k])

            # print(index, location, result)

        return result


s = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(people))
