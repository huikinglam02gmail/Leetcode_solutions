#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#

# @lc code=start
from typing import List
from sortedcontainers import SortedList
class Solution:
    '''
    # Scan rating from left to right
    # After going through an element, place it into a sortedlist data structure
    # We can easily binary search for how many elements are smaller or larger than the current element on its left. Record it.
    # Repeat the procedure, but this time form right to left
    # Finally go through each index, add up left_smaller*right_larger and left_larger*right_smaller for each index    
    '''
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        left_list = SortedList()
        left_smaller, left_larger = [0] * n, [0] * n
        for i in range(n):
            left_smaller[i] = left_list.bisect_left(rating[i])
            left_larger[i] = i - left_smaller[i]
            left_list.add(rating[i])
        right_list = SortedList()
        right_smaller, right_larger = [0] * n, [0] * n
        for i in range(n - 1, -1, -1):
            right_smaller[i] = right_list.bisect_left(rating[i])
            right_larger[i] = n - 1 - i - right_smaller[i]
            right_list.add(rating[i])
        result = 0
        for i in range(n):
            result += left_smaller[i] * right_larger[i]
            result += right_smaller[i] * left_larger[i]
        return result
# @lc code=end

