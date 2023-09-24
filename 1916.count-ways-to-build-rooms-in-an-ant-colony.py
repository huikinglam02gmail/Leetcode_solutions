#
# @lc app=leetcode id=1916 lang=python3
#
# [1916] Count Ways to Build Rooms in an Ant Colony
#

# @lc code=start
import math
from typing import List


class Solution:
    '''
    let dp[node] =  [number of different orders you can build if we start from node, length of chain]
    Why length of chain? Consider the case of Example 2. At 3 or 4, there are no child. So return [1, 1] (1 for itself.)
    Then for 1 or 2, there is only 1 child and it has length of 1. So return [1, 2]
    Now to node 0, Notice we are having two chains of length 2 for each child. So, the answer is (2 + 2)C2 = 6. 
    Therefore, for the chain length, we add up all the chain length in a subtree + 1. And for the answer, we multiply the ans between each branch with (total chain length after merge) C (chain length of branch) (in the end it's the multinomial (total chain length of branches)! / (branch 1 total chain length)! /...). The multiplication means one can any branch at each entry.
    '''
    def dfs(self, node):
        if len(self.graph[node]) == 0:
            return [1, 1]
        else:
            chainLength = 0
            result = 1
            for nxt in self.graph[node]:
                childNumberWays, childChainLength = self.dfs(nxt)
                chainLength += childChainLength
                result *= childNumberWays
                result %= self.MOD
                result *= math.comb(chainLength, childChainLength)
                result %= self.MOD
            return [result, chainLength + 1]

    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        self.MOD = pow(10, 9) + 7
        self.graph = [set() for i in range(len(prevRoom))]
        for i, prev in enumerate(prevRoom):
            if prev >= 0:
                self.graph[prev].add(i)
        return self.dfs(0)[0]
        
# @lc code=end

