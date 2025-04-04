#
# @lc app=leetcode id=3076 lang=python3
#
# [3076] Shortest Uncommon Substring in an Array
#

# @lc code=start
from typing import List


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        hashTable = {}
        localHashTable = [{} for i in range(len(arr))]
        for k, s in enumerate(arr):
            for i in range(len(s)):
                for j in range(i, len(s), 1):
                    hashTable[s[i:j + 1]] = hashTable.get(s[i:j + 1], 0) + 1
                    localHashTable[k][s[i:j + 1]] = localHashTable[k].get(s[i:j + 1], 0) + 1
        result = []
        for k in range(len(arr)):
            candidates = []
            for s in localHashTable[k]:
                if localHashTable[k][s] == hashTable[s]: candidates.append(s)
            candidates.sort(key = lambda x: [len(x), x])
            if len(candidates) == 0: result.append("")
            else: result.append(candidates[0])
        return result
        
# @lc code=end
