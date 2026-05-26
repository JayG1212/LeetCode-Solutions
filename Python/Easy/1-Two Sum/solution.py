class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## Uses O(N) time complexity to solve the problem
        my_dict = {}
        
        for i in range(len(nums)):
            current_num = nums[i]
            num_needed = target - current_num # Calculates the number needed for the current number to equal target
            if(num_needed in my_dict): # If the number needed to equal the target is in the dictionary, we have the ToSum 
                return [my_dict[num_needed], i]
            else:
                my_dict[nums[i]] = i # If not, add the current number to the dictionary