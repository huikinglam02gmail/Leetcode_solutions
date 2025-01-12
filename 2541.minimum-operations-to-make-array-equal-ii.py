#
# @lc app=leetcode id=2541 lang=python3
#
# [2541] Minimum Operations to Make Array Equal II
#

# @lc code=start
from typing import List


class Solution:
    '''
    Only works if diffs sums up to 0
    Put all diffs into sortedList
    '''
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sl = SortedList()
        S = 0
        for num1, num2 in zip(nums1, nums2):
            if num1 != num2 and k == 0: return -1
            if num1 > num2 and (num1 - num2) % k != 0: return -1
            if num2 > num1 and (num2 - num1) % k != 0: return -1
            S += num1 - num2
            if num1 != num2: sl.add(num1 - num2)
        if S != 0: return -1
        result = 0
        while sl:
            smallest = sl.pop(0)
            largest = sl.pop(-1)
            toDeduct = min(abs(smallest), abs(largest))        
            smallest += toDeduct
            if smallest < 0: sl.add(smallest)
            largest -= toDeduct
            if largest > 0: sl.add(largest)
            result += toDeduct // k
        return result

# @lc code=end
