#
# @lc app=leetcode id=2284 lang=python3
#
# [2284] Sender With Largest Word Count
#

# @lc code=start
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hashTable = {}
        currentMax = 0
        currentKey = ""
        for m, s in zip(messages, senders): 
            hashTable[s] = hashTable.get(s, 0) + len(m.split(" "))
            if hashTable[s] > currentMax: 
                currentKey = s
                currentMax = hashTable[s]
            elif hashTable[s] == currentMax and s > currentKey: currentKey = s
        return currentKey
# @lc code=end

