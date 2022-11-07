#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#

# @lc code=start
from typing import List
class Solution:
    # Make use of XOR property
    # Prepare prefix XOR for the array
    # Requirement: i < j, but j <= k
    # a = prefix[j] ^ prefix[i]
    # b = prefix[k+1]^prefix[j]
    # We are looking for prefix[i]^prefix[j] = prefix[k+1]^prefix[j]
    # We can prepare pairwise XOR between all prefix XORs

    def countTriplets(self, arr: List[int]) -> int:
        prefix, n, result = [0], len(arr), 0

        for i, num in enumerate(arr):
            prefix.append(prefix[-1]^num)
        
        hashTableEnd = {}
        for i in range(n):
            for j in range(i+1,n+1):
                pair = prefix[i]^prefix[j]
                if pair not in hashTableEnd:
                    hashTableEnd[pair] = {}
                if j not in hashTableEnd[pair]:
                    hashTableEnd[pair][j] = 0
                hashTableEnd[pair][j] += 1
                if i in hashTableEnd[pair]:
                    result += hashTableEnd[pair][i]
        return result
# @lc code=end

