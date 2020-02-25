class Solution_20200219(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_stack = []
        for item in s:
            if item == '(' or item == '[' or item == '{':
                s_stack.append(item)

            elif item == ')':
                if len(s_stack) != 0 and s_stack[-1] == '(':
                    s_stack.pop()
                else:
                    return False

            elif item == ']':
                if len(s_stack) != 0 and s_stack[-1] == '[':
                    s_stack.pop()
                else:
                    return False
            else:
                if len(s_stack) != 0 and s_stack[-1] == '{':
                    s_stack.pop()
                else:
                    return False
        if len(s_stack) == 0:
            return True
        else:
            return False

solution = Solution_20200219()
print(solution.isValid("("))

