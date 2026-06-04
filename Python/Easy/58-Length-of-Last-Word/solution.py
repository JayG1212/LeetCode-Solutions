class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while s[i] == ' ' and i >= 0:
            i -= 1
        
        count = 0
        while s[i] != ' ' and i >= 0:
            count += 1
            i -= 1
        return count