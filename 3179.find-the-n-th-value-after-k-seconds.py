#
# @lc app=leetcode id=3179 lang=python3
#
# [3179] Find the N-th Value After K Seconds
#

# @lc code=start
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        nums = [1] * n
        MOD = 1000000007
        for i in range(k):
            prefix = [0]
            for num in nums: prefix.append((prefix[-1] + num) % MOD)
            nums = prefix[1:]
        return nums[-1]
# @lc code=end

