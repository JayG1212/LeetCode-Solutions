class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert int x, to a string to index
        string_x = str(x)
        left = 0
        right = len(string_x) - 1
        
        # If the left and right index chars are not the same, return false. If they are, increment and decrement each respective index and repeat until they meet in the middle
        while left < right:
            if string_x[left] != string_x[right]:
                return False
            left += 1
            right -= 1

        return True
        