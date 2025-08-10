#
# @lc app=leetcode id=3633 lang=python3
#
# [3633] Earliest Finish Time for Land and Water Rides I
#

# @lc code=start
import bisect
from operator import itemgetter
from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        result = float("inf")
        for sl, dl in zip(landStartTime, landDuration):
            for sw, dw in zip(waterStartTime, waterDuration):
                if sl + dl <= sw: result = min(result, sw + dw)
                else: result = min(result, sl + dl + dw)
        
        for sw, dw in zip(waterStartTime, waterDuration):
            for sl, dl in zip(landStartTime, landDuration):
                if sw + dw <= sl: result = min(result, sl + dl)
                else: result = min(result, sw + dw + dl)
        return result
# @lc code=end

