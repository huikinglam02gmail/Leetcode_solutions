#
# @lc app=leetcode id=1744 lang=python3
#
# [1744] Can You Eat Your Favorite Candy on Your Favorite Day?
#

# @lc code=start
from typing import List


class Solution:
    '''
    You cannot eat any candy of type i unless you have eaten all candies of type i - 1
    So we need to eat from left to right. Otherwise candy type does not matter
    We first do the prefix sum. prefixSum[i] = number of candies that must be eaten before eating type i
    Therefore minimum of days before starting to eat type i candy is prefixSum[i] // dC
    And maximum of number of days to finish eating type i candy is prefixSum[i + 1] // 1 = prefixSum[i + 1]
    '''
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefixSum = [0]
        for candy in candiesCount:
            prefixSum.append(prefixSum[-1] + candy)
        
        result = []
        for fT, fD, dC in queries:
            result.append(prefixSum[fT] // dC <= fD < prefixSum[fT + 1])
        return result
        
# @lc code=end

