#
# @lc app=leetcode id=1815 lang=python3
#
# [1815] Maximum Number of Groups Getting Fresh Donuts
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    '''
    This problem requires careful thinking about the problem statement. We would like to maximize the number of groups with first person served with fresh donuts. So any group[i] % batchSize == 0 will be eligible.
    Secondly, for group[i] % batchSize = x != 0, we would like to pair it up with groups with group[i] % batchSize = batchsize -  x. We can only take minimum of the two occurrences.
    For what remains, we don't really know which is the best way to proceed. We can use backtracking to test all possible orders. Luckily we have 1 <= batchSize <= 9, we can represent the remaining combination with a string. We also need memoize the remainder
    '''
    @lru_cache(None)
    def dp(self, state, remainder):
        if len(state) == 0: return 0
        result = 1 if remainder == 0 else 0
        extra = 0
        for i in range(len(state)):
            if not (i > 0 and state[i] == state[i - 1]): 
                extra = max(extra, self.dp(state[:i] + state[i+1:], (remainder + int(state[i])) % self.batchSize))
        return result + extra
    
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        counts = [0] * batchSize
        self.batchSize = batchSize
        for group in groups:
            counts[group % batchSize] += 1
        result = counts[0]
        for i in range(1, batchSize // 2 + 1, 1):
            toReduce = min(counts[i], counts[batchSize - i]) if 2 * i != batchSize else counts[i] // 2
            counts[i] -= toReduce
            counts[batchSize - i] -= toReduce
            result += toReduce
        initialState = ""
        for i in range(1, batchSize, 1):
            initialState += str(i) * counts[i]
        return result + self.dp(initialState, 0)
            

