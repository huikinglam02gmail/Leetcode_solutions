#
# @lc app=leetcode id=1621 lang=python3
#
# [1621] Number of Sets of K Non-Overlapping Line Segments
#

# @lc code=start
import math


class Solution:
    # The question is alternatively asking:
    # How many ways to code the combinations?
    # We can represent each segment by two 1s i.e. a segment of length 1 is represented by 11
    # A segment of length 2 is represented by 101 etc.
    # free space is represented by 0 between even and odd count of 1s
    # Then we can represent all combinations by n + k - 1 spots
    # And we are asked the number of combinations to put in 2*k 1s
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, 2 * k) % (pow(10, 9) + 7)
# @lc code=end

