#
# @lc app=leetcode id=1044 lang=python3
#
# [1044] Longest Duplicate Substring
#

# @lc code=start
class Solution:
    '''
    Same kind of question as Leetcode 718. Maximum Length of Repeated Subarray
    To find the Longest Duplicate Substring, we can use binary search to find the answer
    The question to ask is: is there a substring of length L which repeats in the string?
    we binary search for L between 0 and len(s)-1
    To solve the problem, we use the Rabin-Karp algorithm to matching a rolling hash against the pattern's hash
    Base chosen: must be larger than maximum of value of s, preferably prime; Mod: large enough to avoid overflow, should be prime
    Generate a lookup table for pow(self.base, 0:len(s)) % self.MOD
    '''

    def rolling_hash(self, i, size, seed):
        h = seed
        if i == 0:
            for j in range(size):
                h *= self.base
                h += ord(self.string[i + j])-ord('a')
                h %= self.MOD
        else:
            h -= (ord(self.string[i - 1]) - ord('a')) * self.lookup[size - 1]
            h *= self.base
            h += ord(self.string[i + size - 1])-ord('a')
            h %= self.MOD
        return h
 
    def foundSubString(self, size):
        '''
        Go through all substrings with length size in s, and record their hash values and the corresponding index        
        '''
        seen = {}
        h = 0
        for i in range(len(self.string) - size + 1):
            h = self.rolling_hash(i, size, h)
            if h not in seen:
                seen[h] = i
            else:
                j = seen[h]
                if self.string[i : i + size] == self.string[j : j + size]:
                    return [True, j]
        return [False, -1]
    
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        if n == 2:
            if s[0] == s[1]:
                return s[0]
            return ""
        self.base, self.MOD = 29, pow(2,31)-1
        self.lookup = []
        seed = 1
        for i in range(n):
            self.lookup.append(seed)
            seed *= self.base
            seed %= self.MOD
        
        self.string = s
        left, right, startIndex = 1, len(s), -1
        while left < right:
            mid = left + (right - left) // 2
            exist, j = self.foundSubString(mid)
            if exist:
                left = mid + 1
                startIndex = j
            else:
                right = mid
        return self.string[startIndex : startIndex + left - 1] if startIndex != -1 else ""
# @lc code=end

