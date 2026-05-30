class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to check if the popped open bracket matches the closed bracket
        pairs = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }

        # String used to identify open brackets
        open_brackets = '([{' 

        stack = []       
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if(len(stack) != 0):
                    top = stack.pop()
                    if pairs[top] != char:
                        return False
                else:
                    return False
        return len(stack) == 0