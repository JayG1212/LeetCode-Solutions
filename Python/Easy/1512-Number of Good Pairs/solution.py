class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        count = 0
        my_dict = {}

        for num in nums:
            if(num not in my_dict):
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        for key in my_dict:
            n = my_dict[key]
            if(n > 1):
                count += n * (n - 1)//2 # n choose 2
        return count

       