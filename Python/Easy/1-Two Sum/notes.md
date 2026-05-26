# Pattern: Hash Map (Dictionary)
# Time complexity: O(N)
# Reflection:
    The nested loop, O(n^2), solution to this problem was very easy. Thus I wanted to attempt it with a O(N) time complexity.

    I figured it would need a dictionary for the solutions, however I hadn't thought about how we could use the dictionary as a way to verify if the target value was in our list or not.

    Furthermore, I did not initially approach this problem with a mathematical understanding of calculating the target needed for the current number, and checking that way.

    Takeaway:
        Hash Maps can be used to turn nested loop problems into single-pass lookup problems.