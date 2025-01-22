#
# @lc app=leetcode id=2598 lang=python3
#
# [2598] Smallest Missing Non-negative Integer After Operations
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        hashTable = {}
        for num in nums: hashTable[num % value] = hashTable.get(num % value, 0) + 1
        dq = deque()
        for mod in sorted(hashTable.keys()): dq.append([mod, hashTable[mod]])
        cur = 0
        while dq:
            mod, val =  dq.popleft()
            if cur % value != mod: break
            else:
                cur += 1
                val -= 1
                if val > 0: dq.append([mod, val])
        return cur
# @lc code=end

