#
# @lc app=leetcode id=1817 lang=python3
#
# [1817] Finding the Users Active Minutes
#

# @lc code=start
from typing import List


class Solution:
    '''
    Very easy: just use a dictionary <time, hashSet>. return the histogram of size
    '''
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hashTable = {}
        for id, time in logs:
            hashTable[id] = hashTable.get(id, set())
            hashTable[id].add(time)
        result = [0] * k
        for key, valueSet in hashTable.items():
            result[len(valueSet) - 1] += 1
        return result
        
# @lc code=end

