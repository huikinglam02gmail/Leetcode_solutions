#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    '''
    Manacher's algorithm
    '''
    def Manacher(self, s):
        n = len(s)
        LPS = [0] * n
        C = R = 0      # center and radius or the rightmost palindrome
        for i in range(n):
            if i < C + R:         # if there's an overlap
                j = LPS[C - (i - C)]       # reflect
                if j < C + R - i:    # case A
                    LPS[i] = j
                    continue
                elif j > C + R - i:  # case B 
                    LPS[i] = C + R - i
                    continue
                else:                # case C
                    pass
            else:                 # no overlap
                j = 0
            while i - j > 0 and i + j < n - 1 and s[i - j - 1] == s[i + j + 1]:
                j += 1
            LPS[i] = j
            if i + j > C + R:
                C, R = i, j
        return LPS

    def longestPalindrome(self, s: str) -> str:
        # Modify the string so that it's always odd
        new_string = "|"
        for c in s:
            new_string += c + "|"
        
        LPS = self.Manacher(new_string)
        maxLength = 0
        maxIndex = 0
        for i, l in enumerate(LPS):
            if l > maxLength:
                maxLength = l
                maxIndex = i
        
        return new_string[maxIndex - maxLength + 1: maxIndex + maxLength + 1: 2]
# @lc code=end

