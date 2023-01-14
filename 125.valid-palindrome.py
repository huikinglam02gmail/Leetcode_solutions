#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = []
        for c in s:
            if c.isalpha():
                newString.append(c.lower())
            elif c.isnumeric():
                newString.append(c)
        l, r = 0, len(newString) - 1
        while l < r:
            if newString[l] != newString[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
# @lc code=end

