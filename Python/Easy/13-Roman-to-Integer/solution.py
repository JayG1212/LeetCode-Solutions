class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Uses a dictionary to map each Roman numeral to its respective numeric value
        my_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        a_num = 0
        i = len(s) - 1
        # Loops from the end of the string
        while i >= 0:
            if i > 0: # This prevents us from ever using index -1 in our if statements
                if s[i] == 'V' and s[i-1] == 'I':
                    a_num += 4
                    i -= 2
                elif s[i] == 'X' and s[i-1] == 'I':
                    a_num += 9
                    i -= 2
                elif s[i] == 'L' and s[i-1] == 'X':
                    a_num += 40
                    i -= 2
                elif s[i] == 'C' and s[i-1] == 'X':
                    a_num += 90
                    i -= 2
                elif s[i] == 'D' and s[i-1] == 'C':
                    a_num += 400
                    i -= 2
                elif s[i] == 'M' and s[i-1] == 'C':
                    a_num += 900
                    i -= 2
                else:
                    a_num += my_dict[s[i]]
                    i -= 1
            else:
                    a_num += my_dict[s[i]]
                    i -= 1
        return a_num

        
        