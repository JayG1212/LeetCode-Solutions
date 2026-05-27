# Pattern: Hash Map (Dictionary)
# Time complexity: O(N)
# Reflection:
    I had some trouble with my initial implementation of using a lower index dictionary and an upper one for tracking.
    Tha main problem I ran into was when I would encounter the second instance of the lowercase letter which would occur after the first occurrence of the uppercase letter
    The hint in the problem helped me figure this out; where it told me to track the last index of each lowercase char, and the first index of each uppercase char
    This made it much easier and I was able to complete it with three loops.
    I would have preferred to have done it with less loops, and I would have preferred to not have used three dictionaries: the upper one, the lower one, and a tracker to make sure I compare each unique char once in the final loop