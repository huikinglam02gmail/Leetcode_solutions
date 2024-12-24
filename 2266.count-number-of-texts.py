#
# @lc app=leetcode id=2266 lang=python3
#
# [2266] Count Number of Texts
#

# @lc code=start
class Solution:
    '''
    dp[i][4] = [
    # of possible text messages represented by pressedKey[:i + 1], if pressedKey[i] is the 1st repeat, 
    # of possible text messages represented by pressedKey[:i + 1], if pressedKey[i] is the 2nd repeat,
    # of possible text messages represented by pressedKey[:i + 1], if pressedKey[i] is the 3nd repeat, 
    # of possible text messages represented by pressedKey[:i + 1], if pressedKey[i] is the 4th repeat, 
    ]
    '''
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0, 0, 0, 0]
        MOD = 1000000007
        for i, c in enumerate(pressedKeys):
            dpNew = [0, 0, 0, 0]
            if i == 0: dpNew[0] =  1
            elif pressedKeys[i] == pressedKeys[i - 1]:
                dpNew[0] = sum(dp)
                dpNew[1] = dp[0]
                dpNew[2] = dp[1]
                if c == '7' or c == '9': dpNew[3] = dp[2]
            else:
                dpNew[0] = sum(dp)
                dpNew[1] = 0
                dpNew[2] = 0
                dpNew[3] = 0
            for j in range(4): dp[j] = dpNew[j] % MOD
        return sum(dp) % MOD
# @lc code=end

