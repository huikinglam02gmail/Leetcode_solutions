#
# @lc app=leetcode id=2116 lang=python3
#
# [2116] Check if a Parentheses String Can Be Valid
#

# @lc code=start
class Solution:
    '''
    If len(s) is odd: impossible
    Then scan from left to right, keep track of balance: "(" - ")" when we reach balance < 0 and locked[i] == 0, we change s[i] from ")" to "(" and add balance by 2
    We also scan right to left
    '''
    def canBeValid(self, s: str, locked: str) -> bool:
        balance = 0
        n = len(s)
        if n % 2: return False
        for i in range(n):
            if s[i] == "(" or locked[i] == "0": balance += 1
            else: balance -= 1
            if balance < 0: return False
        balance = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ")" or locked[i] == "0": balance += 1
            else: balance -= 1
            if balance < 0: return False
        return True
# @lc code=end

