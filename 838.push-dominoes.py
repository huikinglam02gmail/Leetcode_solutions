#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    '''
    We will adopt a "force field" notation for keeping effect of L and R dominoes
    This is to avoid having to bookkeep distance to nearest L and R
    We do a two-pass scan for L and R respectively
    When the entry is ".", the effect of the previous L or R weaken by 1    
    '''
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left_push = [0 for i in range(n)]
        right_push = [0 for i in range(n)]
        
        for i in range(n):
            if dominoes[i] == "R": right_push[i] = n
            elif dominoes[i] == "L": right_push[i] = 0
            elif i > 0  and right_push[i-1] > 0: right_push[i] = right_push[i-1] - 1
        for i in range(n-1,-1,-1):
            if dominoes[i] == "L": left_push[i] = n
            elif dominoes[i] == "R": left_push[i] = 0
            elif i < n-1  and left_push[i+1] > 0: left_push[i] = left_push[i+1] - 1
        result = ""
        for i, c in enumerate(dominoes):
            if c != ".": result += c
            elif left_push[i] < right_push[i]: result += "R"
            elif left_push[i] > right_push[i]: result += "L"
            else: result += c
        return result
            
# @lc code=end

