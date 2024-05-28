#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    '''
    Typical sliding window problem
    First calculate absolute difference between each corresponding characters between s and t    
    '''
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left, S, result = -1, 0, 0
        for right in range(n):
            S += abs(ord(s[right]) - ord(t[right]))
            while left < right and S >  maxCost:
                left += 1
                S -= abs(ord(s[left]) - ord(t[left]))
            if S <= maxCost: result = max(result, right - left)
        return result
            
            
# @lc code=end

