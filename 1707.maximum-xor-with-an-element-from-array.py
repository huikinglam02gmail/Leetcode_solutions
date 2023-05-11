#
# @lc app=leetcode id=1707 lang=python3
#
# [1707] Maximum XOR With an Element From Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    First sort nums and queries according to m (save the indices as well).
    Then we build nums from small to large, such that it always obey nums[j] <= mi
    In order to find the maximum XOR given each xi, we screen from large to small digits in the binary representation: we prefer numbers giving 1 when XORing with the xi in larger digits. For example x = 2 and m = 10, suppose we have 4 and 8 in nums. 2 is "0010" It would XOR larger with 8 "1000". Therefore we would like to build Trie of the binary representation for each number in nums. 30-level Trie would suffice in the current scenario
    '''
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
# @lc code=end

