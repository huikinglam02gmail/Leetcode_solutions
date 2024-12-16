#
# @lc app=leetcode id=3386 lang=python3
#
# [3386] Button with Longest Push Time
#

# @lc code=start
from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        hashTable = {}
        for i in range(len(events)):
            if i == 0: hashTable[events[i][0]] = events[i][1]
            else: hashTable[events[i][0]] = max(hashTable.get(events[i][0], 0), events[i][1] - events[i - 1][1])
        data = [[k, v] for k, v in hashTable.items()]
        data.sort(key = lambda x: [-x[1], x[0]])
        return data[0][0]
        
# @lc code=end

