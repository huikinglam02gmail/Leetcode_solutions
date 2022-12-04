#
# @lc app=leetcode id=2256 lang=python3
#
# [2256] Minimum Average Difference
#

# @lc code=start
class Solution:
    # Prefix sum would handle the problem nicely
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        minsofar = prefix[-1] // n
        result = n - 1
        for i in range(n-1):
            current = abs(prefix[i+1] // (i + 1) - (prefix[-1] - prefix[i+1]) // (n - i - 1))
            if current < minsofar:
                minsofar = current
                result = i
            elif current == minsofar and i < result:
                result = i
        return result
                        
# @lc code=end

