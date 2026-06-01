class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        i = 1
        while i <= n:
            message = ""
            if(i % 3 == 0):
                message += "Fizz"
            if(i % 5 == 0):
                message += "Buzz"
            if(i % 3 != 0 and i % 5 != 0):
                message = str(i)
            result.append(message)
            i += 1
        return result
            