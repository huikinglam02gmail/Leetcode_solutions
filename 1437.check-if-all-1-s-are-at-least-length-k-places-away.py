#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
class Solution:
    # Minimum length must be between adjacent ones
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = - float('Inf')
        for i, num in enumerate(nums):
            if num == 1:
                if i - prev <= k:
                    return False
                prev = i
        return True

# @lc code=end

