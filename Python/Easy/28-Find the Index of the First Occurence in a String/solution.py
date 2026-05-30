class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_length = len(needle)
        f_index = -1
        i = 0
        while i <= (len(haystack) - n_length) and f_index == -1:
            if haystack[i:i+n_length] == needle:
                f_index = i
            i += 1
        return f_index