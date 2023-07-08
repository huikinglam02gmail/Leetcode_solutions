#
# @lc app=leetcode id=2551 lang=python3
#
# [2551] Put Marbles in Bags
#

# @lc code=start
class Solution:
    '''
    Find k max / min pairs of weights[0] + weights[-1] + (weights[i] + weight[i+1]), i from 0 to n - 2    
    '''

    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        data = []
        for i in range(len(weights) - 1):
            data.append(weights[i] + weights[i+1])
        data.sort()
        return sum(data[(-k + 1):]) - sum(data[:(k - 1)])
        
# @lc code=end

