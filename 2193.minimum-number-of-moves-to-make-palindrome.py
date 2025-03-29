#
# @lc app=leetcode id=2193 lang=python3
#
# [2193] Minimum Number of Moves to Make Palindrome
#

# @lc code=start
class Solution:
    '''
    Keep constructing the palindrome from the right
    '''
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        result = 0
        while s:
            i = s.index(s[-1])
            if i == len(s) - 1: result += i // 2
            else: 
                result += i
                s.pop(i)
            s.pop()
        return result
        
# @lc code=end
