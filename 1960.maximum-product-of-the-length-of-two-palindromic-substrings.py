#
# @lc app=leetcode id=1960 lang=python3
#
# [1960] Maximum Product of the Length of Two Palindromic Substrings
#

# @lc code=start
class Solution:
    '''
    2 <= s.length <= 10^5
    We need to use Manacher's algorithm to get longest palindromic sbstring in O(n) time.
    Then the question becomes: before and including an index i, what is the length of the longest substring?
    To answer that we can use the output from Manacher's algorithm: from the start and end indices of longest palindromic substring centered at each index.
    Then we can register the longest palindromic substrings that starts and ends at an index. Also we should max it against prefix[i + 1] - 2:
    prefix[i] = max(prefix[i], prefix[i + 1] - 2), because if there is a palindromic substring of length l ending at i + 1, it's guaranteed there is one of length l - 2 ending at i
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
    
    def maxProduct(self, s: str) -> int:
        n = len(s)
        LPS = self.Manacher(s)
        prefix = [0] * n
        suffix = [0] * n
        for i, l in enumerate(LPS):
            prefix[i + l] = max(prefix[i + l], 2 * l + 1)
            suffix[i - l] = max(suffix[i - l], 2 * l + 1)
        for i in range(n - 2, -1, -1):
            prefix[i] = max(prefix[i], prefix[i + 1] - 2)
        for i in range(1, n, 1):
            suffix[i] = max(suffix[i], suffix[i - 1] - 2)
        prefixMax = [0] * n
        suffixMax = [0] * n
        cur = 0
        for i in range(n):
            cur = max(cur, prefix[i])
            prefixMax[i] = cur
        cur = 0
        for i in range(n - 1, -1, -1):
            cur = max(cur, suffix[i])
            suffixMax[i] = cur
        result = 0
        for i in range(n - 1):
            result  = max(result, prefixMax[i] * suffixMax[i + 1])
        return result
# @lc code=end

