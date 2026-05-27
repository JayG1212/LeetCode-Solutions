class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 0
        # Adds each lowercase char to the dictionary with its last occurrence's index as its key.
        lower_dict = {}
        for i in range(len(word)):
            if word[i].islower():
                lower_dict[word[i]] = i
        
        # Adds each uppercase char to the dictionary with its first occurrence's index as its key.
        upper_dict = {}
        for j in range(len(word)):
            if word[j].isupper() and word[j] not in upper_dict:
                upper_dict[word[j]] = j
        
        # Checks to see if the char is in both the upper and lower dictionary and compares there index value
        # Uses tracker dictionary to make sure it compares each unique char once
        tracker = {}
        for k in range(len(word)):
            lowercase_char = word[k].lower()
            uppercase_char = word[k].upper()
            if lowercase_char in lower_dict and uppercase_char in upper_dict:
                if upper_dict[uppercase_char] > lower_dict[lowercase_char] and lowercase_char not in tracker:
                    count += 1
                tracker[lowercase_char] = 1     
        
        return count
                