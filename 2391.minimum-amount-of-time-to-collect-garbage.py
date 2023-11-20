#
# @lc app=leetcode id=2391 lang=python3
#
# [2391] Minimum Amount of Time to Collect Garbage
#

# @lc code=start
from typing import List


class Solution:
    '''
    Rather straightforward question
    Use the category as key in hash table and mark where the garbage is
    Use prefix sum to easily look up time to travel between two spots
    Each character will cost 1 minute 
    '''

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        hash_table = {"M": [], "P": [], "G": []}
        for i, junk in enumerate(garbage):
            for c in junk:
                hash_table[c].append(i)
        prefix = [0]
        for t in travel:
            prefix.append(prefix[-1] + t)
        result = 0
        for route in hash_table.values():
            for i in range(len(route)):
                result += 1 + prefix[route[i]] - prefix[i if i == 0 else route[i - 1]]
        return result
        
# @lc code=end

