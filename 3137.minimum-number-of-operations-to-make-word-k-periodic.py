#
# @lc app=leetcode id=3137 lang=python3
#
# [3137] Minimum Number of Operations to Make Word K-Periodic
#

# @lc code=start
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        hashTable = {}
        for i in range(0,len(word),k): hashTable[word[i:i+k]] = hashTable.get(word[i:i+k], 0) + 1
        return len(word) // k - max(hashTable.values())
# @lc code=end

