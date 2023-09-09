#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#

# @lc code=start
class Solution:
    '''
    We first count how many 0 and 1 are at odd and even positions
    cost = min(# 0 in odd + # 1 in even, # 0 in even, # 1 in odd)
    If no type 1 move, the ans is cost
    If we allow type 1 move, for each move, element 0  becomes n - 1 and all other elements shift parity
    keep finding minimum
    '''
    def minFlips(self, s: str) -> int:
        parity = [[0 for i in range(2)] for j in range(2)]
        n = len(s)
        result = n
        for i in range(n):
            parity[i % 2][int(s[i])] += 1
        
        for i in range(n):
            result = min(result, parity[1][0] + parity[0][1])
            result = min(result, parity[0][0] + parity[1][1])
            parity[0][int(s[i])] -= 1
            parity[0][0], parity[1][1], parity[0][1], parity[1][0] = parity[1][0], parity[0][1], parity[1][1], parity[0][0]
            parity[(n - 1) % 2][int(s[i])] += 1
        return result

# @lc code=end

