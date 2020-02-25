# leetcode submit region begin(Prohibit modification and deletion)
class Solution_20200220(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result_list = []
        self.generateCombination("", 0, digits, result_list)
        return result_list

    def generateCombination(self,current_str,current_index, digits, result_list):
        letter_list = [
            [],
            [],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"]
        ]
        if current_index == len(digits):
            result_list.append(current_str)
            return

        num = digits[current_index]
        for letter in letter_list[int(num)]:
            self.generateCombination(current_str + letter, current_index + 1, digits, result_list)

# leetcode submit region end(Prohibit modification and deletion)


solution = Solution_20200220()
result = solution.letterCombinations("23")
print(result)