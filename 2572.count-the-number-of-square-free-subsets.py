#
# @lc app=leetcode id=2572 lang=python3
#
# [2572] Count the Number of Square-Free Subsets
#

# @lc code=start
from typing import List


class Solution:
    '''
    A square-free integer is an integer that is divisible by no square number other than 1.
    Therefore, it must be a product of some primes
    1 <= nums[i] <= 30
    So we only need to concern ourselves with primes smaller than or equal to 30
    Which is 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 => 10 of them
    A subset of the array nums is square-free if the product of its elements is a square-free integer.
    The product of all of a subset's element is a product of the prime factorizations of all items
    To be square free, each prime factor should appear only once
    => It fits the use of bitmasking because each prime could either be absent of appear only once in the subset.
    We therefore use DP to solve this problem
    dp(i, mask) = the number of square-free non-empty subsets of the array nums[i:].
    We are looking for sum(dp(0, :))
    Recurrence relation: 
    given nums[i], we first factorize it into primes.
    if nums[i] = 1, we can include it in all the subsets. So dp[i, mask] = 2 * dp[i + 1, mask] for all mask
    if nums[i] is not square free, we cannot include it in all subsets. So, dp[i, mask] = dp[i + 1, mask] for all mask
    Finally, if nums[i] is square free but not equal to 1, we identify its possible counterparts maskCounterpart.
    numsMask ^ maskCounterpart = mask => maskCounterpart = mask ^ numsMask
    To enforce each prime factor can only once, we check for (mask ^ numsMask) & numMask == 0    
    dp[i, mask] = dp[i + 1, mask] + dp[i + 1, mask ^ numsMask]
    This way, we can consider 1 as having the numsMask = 0. 
    '''
    def getNumMask(self, num):
        mask = 0
        while num > 1:
            for prime in self.primes.keys():
                while num % prime == 0:
                    if (mask & (1 << self.primes[prime])) == 0:
                        mask ^= (1 << self.primes[prime])
                        num //= prime
                    else:
                        return -1
        return mask
    
    def squareFreeSubsets(self, nums: List[int]) -> int:
        self.primes = {2: 0, 3: 1, 5: 2, 7: 3, 11: 4, 13: 5, 17: 6, 19: 7, 23: 8, 29: 9}
        n = len(nums)
        MOD = pow(10, 9) + 7
        dp = [[0 for j in range(1 << 10)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            numMask = self.getNumMask(nums[i])
            if numMask >= 0:
                dp[i][numMask] += 1
            if i < n - 1:
                for mask in range(1 << 10):
                    dp[i][mask] += dp[i + 1][mask]
                    if numMask >= 0 and ((mask ^ numMask) & numMask == 0):
                        dp[i][mask] += dp[i + 1][mask ^ numMask]
        return sum(dp[0][:]) % MOD

# @lc code=end

