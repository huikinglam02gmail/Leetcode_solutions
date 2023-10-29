#
# @lc app=leetcode id=1969 lang=python3
#
# [1969] Minimum Non-Zero Product of the Array Elements
#

# @lc code=start
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1000000007
        largest = pow(2, p) - 1
        secondLargest = largest - 1
        numberOfTimes = pow(2, p - 1) - 1
        return (largest * pow(secondLargest, numberOfTimes, MOD)) % MOD
# @lc code=end

