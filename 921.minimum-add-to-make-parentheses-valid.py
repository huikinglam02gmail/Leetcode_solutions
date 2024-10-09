#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    '''
    In principle we can use a stack to handle this problem
    Just keep a stack and if c == "(", append to the stack
    If we see a ")" and if the stack top is "(", the top got popped.
    If the stack top is "(", it cannot be resolved in later characters
    In here, I will just use a balance check O(1) space to do the same thing    
    '''
    def minAddToMakeValid(self, s: str) -> int:
        balance, ans = 0, 0
        for c in s:
            if c == "(": balance += 1
            else: balance -= 1
            if balance == -1:
                ans += 1
                balance += 1
        return ans + balance
# @lc code=end

