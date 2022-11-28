#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start
import bisect
class Solution:
    # As we are looking for subsequences we are free to sort the array
    # This would help us to locate the minimum of subsequence at left and maximum at right
    # Then for each index, we just binary search for target - nums[i] 
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = pow(10,9) + 7
        pow2 = []
        for i in range(len(nums)):
            if i == 0:
                pow2.append(1)
            else:
                pow2.append((pow2[-1]*2) % MOD)

        nums.sort()
        result = 0
        for i, num in enumerate(nums):
            j = bisect.bisect_right(nums, target - num)
            if j - i > 0:
                result += pow2[j - i - 1]
                result %= MOD
        return result
# @lc code=end

