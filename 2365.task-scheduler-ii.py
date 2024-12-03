#
# @lc app=leetcode id=2365 lang=python3
#
# [2365] Task Scheduler II
#

# @lc code=start
from typing import List


class Solution:
    '''
    use hash table to save for task i, what is the time t in which one can work on it.
    '''
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        hashTable =  {}
        result = 0
        for t in tasks:
            if t in hashTable and hashTable[t] > result: result = hashTable[t]
            result += 1
            hashTable[t] = result + space
        return result
        
# @lc code=end

