#
# @lc app=leetcode id=1616 lang=python3
#
# [1616] Split Two Strings to Make Palindrome
#

# @lc code=start
class Solution:
    # Use two pointers
    # If a[:i] + b[i:] is palindrome, they must match in the ends
    # When we see mismatch a[i] != b[n - 1 - i], the only hope it is still a palidndrome is 
    # b[i: n- i] or a[i: n - i] is a palindrome

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    def canFormPalindrome(self, s1, s2):
        l, r = 0, len(s1) - 1
        canForm = True
        while l < (len(s1) // 2) and s1[l] == s2[r]:
            l += 1
            r -= 1
        if l < (len(s1) // 2):
            canForm = (self.isPalindrome(s1[l : len(s1) - l]) or self.isPalindrome(s2[l : len(s1) - l]))
        return canForm

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.canFormPalindrome(a, b) or self.canFormPalindrome(b, a)

# @lc code=end

