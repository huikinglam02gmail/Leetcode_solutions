#
# @lc app=leetcode id=2566 lang=python3
#
# [2566] Maximum Difference by Remapping a Digit
#

# @lc code=start
class Solution:
    '''
    There are only 10 digits. In terms of a map, there are 100 keys. Use the 100 keys and record max and min of the result and take the difference.
    '''
    def minMaxDifference(self, num: int) -> int:
        master = [int(c) for c in str(num)]
        minResult = float("inf")
        maxResult = - float("inf")
        for i in range(10):
            if i in master:
                for j in range(10):
                    modified = 0
                    for k in range(len(master)):
                        if master[k] == i: modified += j
                        else: modified += master[k]
                        modified *= 10
                    minResult = min(minResult, modified // 10)
                    maxResult = max(maxResult, modified // 10)
        return maxResult - minResult      
                
# @lc code=end

