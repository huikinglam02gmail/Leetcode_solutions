#
# @lc app=leetcode id=2080 lang=python3
#
# [2080] Range Frequency Queries
#

# @lc code=start
import bisect
from typing import List


class RangeFreqQuery:
    '''
    Record value: [indices of appearance]
    Then binary search
    '''

    def __init__(self, arr: List[int]):
        self.appear = {}
        for i in range(len(arr)):
            if arr[i] not in self.appear: self.appear[arr[i]] = []
            self.appear[arr[i]].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.appear: return 0
        else: return bisect.bisect_right(self.appear[value], right) - bisect.bisect_left(self.appear[value], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end

