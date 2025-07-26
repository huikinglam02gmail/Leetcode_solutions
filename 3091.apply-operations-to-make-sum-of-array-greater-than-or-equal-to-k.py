#
# @lc app=leetcode id=3091 lang=python3
#
# [3091] Apply Operations to Make Sum of Array Greater Than or Equal to k
#

# @lc code=start
class Solution:
    '''
    The order of operations should be:
    1. Add 1 to 1 a - 1 times, so that it becomes [a]
    2. Keep duplicating b - 1 times, such that a * b >= k
    Total number of operations n = a + b - 2
    '''
    def minOperations(self, k: int) -> int:
        a = 1
        b = k
        result = a + b - 2
        while a < b:
            a += 1
            while a * b >= k: b -= 1
            result = min(result, a + b - 1)
        return result

# @lc code=end

