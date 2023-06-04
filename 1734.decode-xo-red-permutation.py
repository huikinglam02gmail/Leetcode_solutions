#
# @lc app=leetcode id=1734 lang=python3
#
# [1734] Decode XORed Permutation
#

# @lc code=start
from typing import List


class Solution:
    '''
    We know total XOR of the perm: 1^2^...^n
    To get the result, we only need to know perm[0]
    Now notice n is odd. Let's take n = 5 for a visual example
    Suppose perm = [perm[0], perm[1], perm[2], perm[3], perm[4]]
    encoded = [perm[0]^perm[1], perm[1]^perm[2], perm[2]^perm[3], perm[3]^perm[4]]
    we also know perm[0]^perm[1]^perm[2]^perm[3]^perm[4] = 1^2^3^4^5 = perm[0]^encoded[1]^encoded[3]
    But we are given the encoded. Then perm[0] = 1^2^3^4^5^encoded[1]^encoded[3]
    Given perm[0] and encoded, we recover the whole perm 
    '''
    def decode(self, encoded: List[int]) -> List[int]:
        total = 0
        n = len(encoded) + 1
        for i in range(1, n + 1, 1):
            total ^= i
        initial = total
        for i in range(1, n, 2):
            initial ^= encoded[i]
        result = []
        result.append(initial)
        for i in range(n - 1):
            result.append(result[-1]^encoded[i])
        return result
# @lc code=end

