class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_count=0
        r_count=0
        split_total=0
        for item in s:
            if item == 'R':
                r_count += 1
            else:
                l_count += 1
            if r_count == l_count:
                split_total += 1
                r_count = 0
                l_count = 0
        return split_total

test_str = "LRLRLLRR"
s=Solution()
result = s.balancedStringSplit(test_str)
print(result)