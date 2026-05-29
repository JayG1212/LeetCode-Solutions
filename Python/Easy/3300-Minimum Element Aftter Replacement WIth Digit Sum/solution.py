class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_list = []
        for num in nums:
            count = 0
            str_num = str(num)
            for i in range(len(str_num)):
                count += int(str_num[i])
            new_list.append(count)
        
        return min(new_list)