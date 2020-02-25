"""
    计算二进制数字中有多少个1
    计算数字中二进制有多少个1

解析：
首先是一个数减1，对应二进制的变化就是最右的一个1变为0，而这个1右边的所有0变为1

即相当于包括最后一个1在内的右边所有位取反，例如12（1100）减1，得到11（1011），然后再与变化前的数12（1100）进行与&运算，得到8（1000），
可以看出经过这样一个运算之后这个数的1的个数减少了一个（12和8相差一位），所以可以利用这个原理，得到res[i]=res[i&(i-1)]+1

"""
class Solution(object):
    def countBits(self, num):
        """
        方法1： 逐个/2 是最笨的方法，时间复杂度是 n*lng的复杂度；空间为o(1)
        :type num: int
        :rtype: List[int]
        """
        result = []
        for cur in range(0, num+1):
            # 逐一计算每个数字有多少个二进制
            count = 0
            while cur != 0:
                count += cur % 2
                cur = int(cur / 2)
            result.append(int(count))
        return result

s = Solution()
print(s.countBits(5))

