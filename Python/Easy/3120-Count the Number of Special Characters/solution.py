class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Initializes variables
        my_dict = {}
        count = 0

        # Adds each lowercase letter to the dictionary
        for char in word:
            if char not in my_dict and char.islower():
                my_dict[char] = 1

        # Checks each uppercase char to see if its lowercase equivalent is in the dictionary
        # Increments count if it is
        for char in word:
            if char.isupper():
                if char.lower() in my_dict and my_dict[char.lower()] != 2:
                    my_dict[char.lower()] += 1
                    count += 1
        
        return count