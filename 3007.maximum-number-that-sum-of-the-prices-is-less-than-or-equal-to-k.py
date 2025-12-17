#
# @lc app=leetcode id=3007 lang=python3
#
# [3007] Maximum Number That Sum of the Prices Is Less Than or Equal to K
#

# @lc code=start
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        l, r = 0, pow(2, 49) 
        while l < r: 
            mid = l + (r - l) // 2
            if self.calcPrice(mid, x) <= k:
                l = mid + 1
            else:
                r = mid
        return l - 1
    
    def calcPrice(self, num: int, x: int) -> int:
        result = 0
        for i in range(x - 1, 50, x):
            SegmentSize = pow(2, i + 1)
            factor = num // SegmentSize
            result += pow(2, i) * factor
            extraSegmentStart = SegmentSize * factor
            result += max(0, num - extraSegmentStart - pow(2, i) + 1)
        return result


# @lc code=end
