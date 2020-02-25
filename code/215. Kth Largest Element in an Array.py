"""
    必知必会问题！
    第k大问题，快排

    k在排序中，并不一定
"""

class Solution(object):
    def quickSort(self, num, begin, end, k):
        """
        快排 # 从大到小排列
        :param num:
        :param begin:
        :param end:
        :param k:
        :return:
        """
        #print(num)
        if begin >= end:
            return

        # i、j的条件要格外控制好，不然可能会卡住【3,3,3,3】两个指针都不向前
        # 找到第一个比开始元素小的
        i = begin
        # 找到第一个比开始元素大的
        j = end+1
        while True:
            i += 1
            while i < end and num[i] > num[begin]:
                i += 1
            j -= 1
            while j > begin and num[j] < num[begin]:
                j -= 1
            if i < j:
                # 交换
                tmp = num[i]
                num[i] = num[j]
                num[j] = tmp
            else:
                break

        # 交换 begin和j
        tmp = num[j]
        num[j] = num[begin]
        num[begin] = tmp
        # 此时 j左面的都小于j；j右面的都大于j

        if j+1 == k:
            return
        if j+1 > k:
            self.quickSort(num, begin, j-1, k)
        else:
            # 向右找
            self.quickSort(num, j+1, end, k)


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quickSort(nums, 0,len(nums)-1,k)
        #print(nums)
        return nums[k-1]


nums =[3,3,3,3,2,1]
k = 5
s = Solution()
print(s.findKthLargest(nums,k))