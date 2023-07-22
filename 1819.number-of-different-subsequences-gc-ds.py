#
# @lc app=leetcode id=1819 lang=python3
#
# [1819] Number of Different Subsequences GCDs
#

# @lc code=start
import math
from typing import List


class Solution:
    '''
    This is not a DP problem. Rather, the solution is quite brute force: we just test i in [1, max(nums)] whether it is the GCD of a subsequence inside nums. To test that, simply increment x = i, 2*i,.... up till max(nums). Initialize the gcd as 0. if j * i is inside nums, For example, if nums = [4, 8, 12], we first test x = 1. We see that 4 * 1 is inside nums, and now the gcd is 4. Next we test 8 * 1 is inside nums, but the gcd of 8 with 4 is still 4. Until we reach 12, we see that gcd(12, 4) = 4 != 1, so 1 is not subsequence gcd
    '''
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        numsSet = set(nums)
        T = max(nums) + 1
        res = 0
        for x in range(1, T, 1):
            g = 0
            for y in range(x, T, x):
                if y in numsSet:
                    g = math.gcd(g, y)
                if g == x:
                    res += 1
                    break
        return res
        
# @lc code=end

