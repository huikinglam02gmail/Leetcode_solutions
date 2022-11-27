#
# @lc app=leetcode id=446 lang=python3
#
# [446] Arithmetic Slices II - Subsequence
#

# @lc code=start
class Solution:
    # dp[i][diff] = number of subsequences ending with nums[i] with difference of diff

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        dp =  [{} for i in range(n)]
        result = 0
        for i in range(1,n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # Add all previous elements as first step
                if diff not in dp[i]:
                    dp[i][diff] = 0
                dp[i][diff] += 1
                # look for longer subsequence
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]             
        return result
# @lc code=end

