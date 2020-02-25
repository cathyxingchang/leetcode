class Solution20200218(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        难点在于
        """
        if x == 0:
            return x
        if x> 2**31-1 or x< - (2**31):
            return 0
        str_x = str(x)
        result = ""
        if str_x[0] == '-':
            result = "-"
            i = len(str_x) - 1
            while str_x[i] == '0':
                i -= 1
            while i >= 1:
                result += str_x[i]
                i -= 1
        else:
            i = len(str_x) - 1
            while str_x[i] == '0':
                i -= 1
            while i >= 0:
                result += str_x[i]
                i -= 1
        if int(result) > 2 ** 31 - 1 or int(result) < - (2 ** 31):
            return 0
        return result


solution = Solution20200218()
x = -12303300
print(solution.reverse(x))




