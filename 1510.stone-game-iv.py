#
# @lc app=leetcode id=1510 lang=python3
#
# [1510] Stone Game IV
#

# @lc code=start
class Solution:
    # Get all the square numbers below n
    # Then use dp to solve the problem
    # dp[i] = true if Alices will win the game if it's Alice's turn
    # dp[sq] = true
    
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n + 1)
        perfectSquares = []
        x = 1
        for i in range(1, n + 1):
            if x*x == i:
                dp[i] = True
                perfectSquares.append(i)
                x += 1
            else:
                j = 0
                found_ok = False
                while j < len(perfectSquares) and not found_ok:
                    if not dp[i - perfectSquares[j]]:
                        found_ok = True
                        dp[i] = True
                    else:
                        j += 1        
        return dp[n]
# @lc code=end

