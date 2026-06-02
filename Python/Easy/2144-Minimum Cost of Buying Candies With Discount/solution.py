class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        index = len(cost) - 1
        counter = 0
        minimum_cost = 0
        while index >= 0:
            if counter != 2:
                minimum_cost += cost[index]
                counter += 1
            else:
                counter = 0
            index -= 1
            
        return minimum_cost