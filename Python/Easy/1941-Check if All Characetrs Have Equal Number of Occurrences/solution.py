class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_dict = {}
        for char in s:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1
        occurrences = my_dict[s[0]] 
        for key in my_dict:
            if my_dict[key] != occurrences:
                return False
        return True