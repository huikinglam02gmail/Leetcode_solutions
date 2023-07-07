#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
class Solution:
    '''
    This is the same problem as 424. Longest Repeating Character Replacement
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

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return self.characterReplacement(answerKey, k)
        
# @lc code=end

