class Solution20200218(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        题目要求：不要变成一个转换成一个string来做
        """
        if x < 0:
            return False
        reverse_num = 0
        tmp = x
        while tmp > 0:
            reverse_num = reverse_num*10 + tmp % 10
            tmp = int(tmp/10)
        print(reverse_num)
        if x == reverse_num:
            return True
        return False


solution = Solution20200218()
x = 123
result = solution.isPalindrome(x)
print(result)



