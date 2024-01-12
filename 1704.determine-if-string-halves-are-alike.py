#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        left_count = 0
        for i in range(0,len(s)//2,1):
            if s[i] in vowels:
                left_count += 1
        right_count = 0
        for i in range(len(s)//2,len(s),1):
            if s[i] in vowels:
                right_count += 1
        return left_count == right_count
# @lc code=end

