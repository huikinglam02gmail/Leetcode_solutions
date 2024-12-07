#
# @lc app=leetcode id=1760 lang=python3
#
# [1760] Minimum Limit of Balls in a Bag
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= maxOperations, nums[i] <= 10^9: we know using priority queue is not a good idea
    let's frame the question differently, suppose ans is the final answer. How many operations to get there?
    suppose we have nums[i] = 8 and ans is 3.
    The division procedure that minimizes operation is 8 -> [3, 5] - > [3, 3, 2], with 2 = 8 // 3 operations
    And we know with ans increasing, the number of operations decreases.
    So binary search is the answer to this question
    '''
    def operationsToMake(self, maxN):
        result = 0
        for num in self.nums:
            result += num // maxN
            if num % maxN == 0: result -= 1
        return result

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        self.nums = nums
        l, r = 1, max(self.nums)
        while l < r:
            mid = l + (r - l) // 2
            if self.operationsToMake(mid) <= maxOperations:
                r = mid
            else:
                l = mid + 1
        return l
# @lc code=end

