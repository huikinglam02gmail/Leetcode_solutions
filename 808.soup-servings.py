#
# @lc app=leetcode id=808 lang=python3
#
# [808] Soup Servings
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    Operation 1: A -= 100
    Operation 2: A -= 75, B -= 25
    Operation 3: A -= 50, B -= 50
    Operation 4: A -= 25, B -= 75
    Maintain status of A and B and round
    Since after each round, the modification will add 1/(4^k) to the probability
    We can see that when n becomes large, the answer goes towards 1. To find out the exact limit I manually binary search on the n threshold and found it to be 4801   
    '''
    @lru_cache(None)
    def dfs(self, A, B, k):
        if A <= 0 and B > 0:
            return 1 / pow(4,k)
        if A <= 0 and B <= 0:
            return 1 / (2 * pow(4,k))
        if A > 0 and B <= 0:
            return 0
        result = 0
        result += self.dfs(A - 100, B, k + 1)
        result += self.dfs(A - 75, B - 25, k + 1)
        result += self.dfs(A - 50, B - 50, k + 1)
        result += self.dfs(A - 25, B - 75, k + 1)
        return result
            
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        else:
            return self.dfs(n,n,0)
# @lc code=end

