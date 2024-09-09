#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#

# @lc code=start
from typing import List


class Solution:
    '''
    use prefix Sum and record the min and max seen.
    ans = max(0, upper - lower + 1 - maxSeen + minSeen)
    '''
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        maxSeen = 0
        minSeen = 0
        for diff in differences:
            prefix += diff
            maxSeen = max(maxSeen, prefix)
            minSeen = min(minSeen, prefix)
        return max(0, upper - lower + 1 - maxSeen + minSeen)
# @lc code=end
