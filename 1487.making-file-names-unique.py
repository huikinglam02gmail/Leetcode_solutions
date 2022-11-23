#
# @lc app=leetcode id=1487 lang=python3
#
# [1487] Making File Names Unique
#

# @lc code=start
from typing import List

class Solution:
    # Use hash table to store the next available key
    def getFolderNames(self, names: List[str]) -> List[str]:
        nextName = {}
        for name in names:
            newName = name
            if newName in nextName:
                nextNameID = nextName[newName]
                while newName in nextName:
                    nextNameID += 1
                    newName = name + '(' + str(nextNameID) + ')'
                nextName[name] = nextNameID
            nextName[newName] = 0
        return nextName.keys()
# @lc code=end

