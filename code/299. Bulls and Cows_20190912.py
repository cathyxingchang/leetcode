
"""
    两圈了遍历，第一遍找到相同的；第二遍找到；空间复杂度也很大，额外开了一个数组
    待优化成一个数组的
"""
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_hash = {}
        guess_unlocation = []
        correct = 0
        unmatch = 0
        for index in range(0, len(secret)):
            if secret[index] == guess[index]:
                correct += 1
            else:
                if secret[index] in secret_hash.keys():
                    secret_hash[secret[index]] += 1
                else:
                    secret_hash[secret[index]] = 1
                guess_unlocation.append(guess[index])
        for item in guess_unlocation:
            if item in secret_hash.keys():
                if secret_hash[item] >= 1:
                    unmatch += 1
                    secret_hash[item] -= 1
                pass
        return str(correct) + "A" + str(unmatch) + "B"

#


#

# s = Solution()
# result = s.getHint("1122","2211")
# print(result)





