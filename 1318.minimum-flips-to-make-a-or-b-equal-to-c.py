#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
class Solution:
    '''
    minimum change: for each digit, see if digit[a] | digit[b] == digit[c]
    if digit[c] == 0: result += (digit[a] == 1) + (digit[b] == 1)
    else: result += max(1, (digit[a] == 0) + (digit[b] == 0)) - 1    
    '''
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        for i in range(32):
            if c & (1<<i) == 0:
                result += int(a & (1<<i) != 0) + int(b & (1<<i) != 0)
            else:
                result += max(1, int(a & (1<<i) == 0) + int(b & (1<<i) == 0)) - 1
        return result
                          
# @lc code=end

