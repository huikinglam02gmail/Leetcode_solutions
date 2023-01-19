#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from typing import List


class Solution:
    # Example: [4,5,0,-2,-3,1]
    # Prefix sum = [0,4,9,9,7,4,5]
    # all subarray sum = prefix[j] - prefix[i] for j > i
    # if any sum being divisible by k, prefix[j] % k = prefix[i] % k
    # Now it comes down to this: if we find prefix[i] % k for all element, and record their index of appearance, we should be able to find final number by (n-1)*n // 2 for each index
    # Prefix sum = [0,4,9,9,7,4,5], k = 5
    # % 5:
    # [0, 4, 4, 4, 2, 4, 0]
    # {0: [0,6], 4: [1,2,3,5], 2: [4]}
    # total: 1*2/2 + 3*4/2 = 1+6 = 7 
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix, hash_table = 0, {0: 1}
        for num in nums:
            prefix = (prefix + num) % k
            if prefix not in hash_table:
                hash_table[prefix] = 0
            hash_table[prefix] += 1
        result = 0
        for key in list(hash_table.keys()):
            n = hash_table[key]
            result += n*(n-1) // 2
        return result
# @lc code=end

