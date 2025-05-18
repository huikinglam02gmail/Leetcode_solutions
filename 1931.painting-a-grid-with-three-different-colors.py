#
# @lc app=leetcode id=1931 lang=python3
#
# [1931] Painting a Grid With Three Different Colors
#

# @lc code=start
from collections import deque


class Solution:
    '''
    1 <= m <= 5
    1 <= n <= 1000
    So we add columns from left to right
    We have 3 colors, so we can represent each state of each cell with a bitmask of size 3: state = [001 or 010 or 100], and to consider each row, we shift the state: state << 3, and keep adding. 
    '''
    def statesAreCompatible(self, state1, state2):
        while state1 > 0 and state2 > 0:
            if state1 % (1 << 3) == state2 % (1 << 3): return False
            state1 >>= 3
            state2 >>= 3
        return True

    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = pow(10, 9) + 7
        dq = deque()
        steps = 0
        dq.append(0)
        while dq and steps < m:
            for i in range(len(dq)):
                state = dq.popleft()
                newState = state << 3
                for j in range(3):
                    if state % (1 << 3) != (1 << j):
                        dq.append(newState ^ (1 << j))
            steps += 1

        if n == 1: return len(dq)        

        possibleStates = []
        while dq: possibleStates.append(dq.popleft())

        currentToPrevMap = {}
        for key in possibleStates:
            currentToPrevMap[key] = set()
            for key1 in  possibleStates:
                if self.statesAreCompatible(key, key1): currentToPrevMap[key].add(key1)

        dp = {}
        for key in possibleStates:
            dp[key] = 1
        
        for j in range(1, n):
            dpNew = {}
            for key in currentToPrevMap:
                dpNew[key] = 0
                for oldKey in currentToPrevMap[key]:
                    dpNew[key] += dp[oldKey]
                    dpNew[key] %= MOD
            dp = dpNew

        result = 0
        for key in dp:
            result += dp[key]
            result %= MOD
        return result
                
        
# @lc code=end

