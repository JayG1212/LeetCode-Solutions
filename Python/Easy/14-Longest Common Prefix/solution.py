class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        my_dict = {}

        # Adds every combination of chars in each word to a dictionary as a prefix
        # Increments each prefixes key when encountered
        for word in strs:
            prefix = ""
            for i in range(len(word)):
                prefix += word[i]
                if prefix not in my_dict:
                    my_dict[prefix] = 1
                else:
                    my_dict[prefix] += 1
        
        longest_prefix = ""
        # Creates another dictionary that stores the prefixes that are shared in every word.
        # And adds the length of each prefix as its key
        common_prefixes = {}
        for prefix, count in my_dict.items():
            if count == len(strs): 
                common_prefixes[prefix] = len(prefix)
        
        # If dictionary is empty return an empty string
        # Else, return the prefix with largest key value (Length of prefix)
        if not common_prefixes:
            return ""
        else:
            return max(common_prefixes, key= common_prefixes.get)