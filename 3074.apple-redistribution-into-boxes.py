#
# @lc app=leetcode id=3074 lang=python3
#
# [3074] Apple Redistribution into Boxes
#

# @lc code=start
import bisect
from typing import List


class Solution:
    '''
    sort capacity from large to small, prepare prefix sum
    then one binary search for sum(apple)
    '''
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        prefix = [0]
        for c in capacity: prefix.append(prefix[-1] + c)
        return bisect.bisect_left(prefix, sum(apple))
# @lc code=end

