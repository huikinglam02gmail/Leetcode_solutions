#
# @lc app=leetcode id=2081 lang=python3
#
# [2081] Sum of k-Mirror Numbers
#

# @lc code=start
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        palindromes = set()
        palindromes.add('')
        kMirror = set()
        for i in range(k): 
            palindromes.add(str(i))
            if i > 0:
                kMirror.add(int(str(i), k))
                if len(kMirror) == n: return sum(kMirror)
        
        while len(kMirror) < n:
            l = len(palindromes)
            newPalindromes = set()
            for p in palindromes:
                for i in range(k): 
                    newPalindromes.add(str(i) + p + str(i))
                    if i > 0 and self.isPalindrome(str(int(str(i) + p + str(i), k))):
                        kMirror.add(int(str(i) + p + str(i), k))
            palindromes = palindromes.union(newPalindromes)
        return sum(sorted(kMirror)[:n])

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
        
# @lc code=end
