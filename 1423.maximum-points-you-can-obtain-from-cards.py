#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    # As hinted, we can find sliding window min of n-k sum
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + cardPoints[i])
        result = 0
        for i in range(n-k,n+1,1):
            result = max(prefix[-1] - prefix[i] + prefix[k+i-n], result)
        return result
            
# @lc code=end

