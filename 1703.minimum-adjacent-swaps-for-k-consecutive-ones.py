#
# @lc app=leetcode id=1703 lang=python3
#
# [1703] Minimum Adjacent Swaps for K Consecutive Ones
#

# @lc code=start
from typing import List


class Solution:
    '''
    Remember one key point: the median of a sequence is where we should move all sequence elements to if we want to make all elements equal (Leetcode 462).
    So we record occurence of 1 in nums. Then we consider k subarrays and decide how many moves to create a consecutive k 1s around the median
    '''
    def minMoves(self, nums: List[int], k: int) -> int:
        
# @lc code=end

