#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#

# @lc code=start
from typing import List
class Solution:
    # The problem is asking for contiguous nonempty subarrays which have equal XOR
    # But we XOR them together, we will always arrive at 0
    # So the problem is to find all subarrays with 0 XOR
    # Each with contribute len(0 XOR subarray) - 1 to the result

    def countTriplets(self, arr: List[int]) -> int:
        
# @lc code=end

