#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        for i, num in enumerate(nums):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1] + 1):
                result.append(str(num))
            elif i > 0 and nums[i] == nums[i - 1] + 1:
                ind = result[-1].find("->")
                if ind >= 0:
                    result[-1] = result[-1][:ind] + "->" + str(num)
                else:
                    result[-1] += "->" + str(num)
        return result

# @lc code=end

