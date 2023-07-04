#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
from typing import List


class Solution:
    '''
    use two number to record the occurrence of once and twice appeared number. Initialize them with 0. When a new number comes, we XOR against one. If it occurred:
    1. 0 times, XORing it with one will add it to one
    2. 1 times, XORing it with one will remove it from one. Then we XOR two against the number
    3. 2 times, it is already in two and not in one. To avoid adding to one, we & (one ^ nums[i]) with ~two. Because we used the bitwise complement, we also have to and (twos ^ num) against ~ones

    '''
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
# @lc code=end

