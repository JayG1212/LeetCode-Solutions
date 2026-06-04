class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
       
        i = len(digits) - 1 # Start from end of array

        # First Case: Last digit is less than 9
        # Increment last digit by 1, array same size and only the last element changes
        if digits[i] != 9:
            digits[i] += 1
        # Second and third case: Requires more than element to change because ith elment is 9
        else:
            # Changes each 9 to 0
            while digits[i] == 9 and i >= 0:
                digits[i] = 0
                i -= 1
            # If I is less than 0, every number was 9, meaning we need to add a new 0 to the end of the array
            if i < 0:
                digits[0] = 1
                digits.append(0)
            # If I isn't less than 0, we increment the last number in the array that isn't equal to 9
            else:
                digits[i] += 1
       
        return digits
             
        