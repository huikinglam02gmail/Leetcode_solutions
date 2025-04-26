#
# @lc app=leetcode id=2845 lang=python3
#
# [2845] Count of Interesting Subarrays
#

# @lc code=start
from typing import List


class Solution:
    '''
    let count[i] = count of indices inside nums[:i] which nums[j] % modulo == k, for j < i
    Then for each i, we look for number of js (j < i) in which (counts[i] - counts[j]) % modulo == k
    Rewriting, counts[j] % modulo = (counts[i] + modulo - k) % modulo
    '''
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        counts = [0]
        for num in nums:
            counts.append(counts[-1])
            if num % modulo == k: counts[-1] += 1
        hashTable = {}
        result = 0
        for count in counts:
            result += hashTable.get((count + modulo - k) % modulo, 0)
            hashTable[count % modulo] = hashTable.get(count % modulo, 0) + 1
        return result
# @lc code=end

