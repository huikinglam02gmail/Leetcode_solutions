#
# @lc app=leetcode id=1663 lang=python3
#
# [1663] Smallest String With A Given Numeric Value
#

# @lc code=start
class Solution:
    '''
    We notice that given the same score, we always place smaller character at front. Also, if possible we should always place the smallest character possible at front unless what's left behind cannot hold max characters anymore
    '''
    def getSmallestString(self, n: int, k: int) -> str:
        result = []
        for i in range(1, n + 1, 1):
            chInd = max(1, k - 26 * (n - i))
            chToPut = chr(chInd + ord('a')- 1)
            result.append(chToPut)
            k -= chInd
        return ''.join(result)
# @lc code=end

