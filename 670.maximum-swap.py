#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    '''
    0 <= num <= 10 ^ 8
    just brute force
    '''
    def maximumSwap(self, num: int) -> int:
        numString = [c for c in str(num)]
        maxSoFar = num
        for i in range(len(numString) - 1):
            for j in range(i + 1, len(numString)):
                if int(numString[i]) < int(numString[j]):
                    numString[i], numString[j] = numString[j], numString[i]
                    maxSoFar = max(maxSoFar, int("".join(numString)))
                    numString[i], numString[j] = numString[j], numString[i]
        return maxSoFar
# @lc code=end

