#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    '''
    sliding window: maximize length of the window while satisfying len(window) - # of most frequent <= k 
    '''
    def characterReplacement(self, s: str, k: int) -> int:        
        left, right = 0, 0
        occur = [0]*26
        result = 0
        while right < len(s):
            if right - left - max(occur) <= k:
                result = max(result, right - left)
                occur[ord(s[right]) - ord('A')] += 1
                right += 1
            else:
                occur[ord(s[left]) - ord('A')] -= 1
                left += 1
        if right - left - max(occur) <= k:
            result = max(result, right - left)
        return result
            
# @lc code=end

