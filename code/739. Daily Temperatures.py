"""
    题意：找到后面第一大个比自己大的数字的位置
    medium
"""


class Solution(object):
    def dailyTemperatures_1(self, T):
        """
        这种最简单的策略 肯定是会超时的..人家可是个medium题
        :type T: List[int]
        :rtype: List[int]
        """
        result = []
        for index in range(0,len(T)):
            location = 0
            for compare_index in range(index+1, len(T)):
                if T[compare_index] > T[index]:
                    location = compare_index - index
                    break
            result.append(location)
        return result

    def dailyTemperatures_3(self, T):
        """
        策略2：
        还是超时的
        从后往前，同时记录最大的元素
            如果后面存在比当前大的，则向后找，如果没有就置为0

        :param T:
        :return:
        """
        T = T[::-1]
        max_num = T[0]
        result = [0]
        for index in range(1,len(T)):
            if T[index] < max_num:
                # 有比当前温度高额
                for compare_index in range(index-1, -1, -1):
                    if T[compare_index] > T[index]:
                        location = index - compare_index
                        result.append(location)
                        break
            else:
                result.append(0)
                max_num = T[index]
        return result[::-1]

    def dailyTemperatures(self, T):
        """
        换一种思路思考：每进来一个元素，考虑它之前的元素

        :param T:
        :return:
        """
        result = [0 for i in range(0,len(T))]
        # 构造递减栈，存储元素下标，每进来一个元素，把比它小的都剔除栈
        t_stack = [0]
        for index in range(1, len(T)):
            while len(t_stack) != 0 and T[index] > T[t_stack[-1]]:
                result[t_stack[-1]] = index - t_stack[-1]
                t_stack.pop()
            t_stack.append(index)
        return result




s = Solution()
T = [1,9,4,5]
print(s.dailyTemperatures(T))




