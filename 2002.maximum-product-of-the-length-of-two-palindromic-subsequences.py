#
# @lc app=leetcode id=2002 lang=python3
#
# [2002] Maximum Product of the Length of Two Palindromic Subsequences
#

# @lc code=start
class Solution:
    '''
    2 <= s.length <= 12
    so we can use bitmask to represent which bits are used
    First thing to do: for each mask, determine if the mask represent a palindrome O(2 ^ 12)
    Then among the mask, determine if the subMasks of 0 ^ mask is inside the set
    '''
    '''
    Python program to decide is a string is a palindrome
    '''
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return False
            else: 
                l += 1
                r -= 1
        return True
    
    '''
    Method to return all subset of set bits of num1 while smaller than num2
    '''
    def setBits(self, num1, num2):
        result = set()
        temp = num1
        while temp > 0:
            if temp <= num2:
                result.add(temp)
            temp -= 1
            temp &= num1
        return result
    
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindromes =  {}
        for mask in range(1, 1 << n):
            sMask, count = "", 0
            for i in range(n - 1, -1, -1):
                if mask & (1 << i) > 0:
                    sMask += s[i]
                    count += 1
            if self.isPalindrome(sMask): palindromes[mask] = count
        
        result = 0
        for mask in range(1 << n):
            if mask in palindromes:
                antiMaskSet = self.setBits(((1 << n) - 1) ^ mask, 1 << n)
                for aMask in antiMaskSet:
                    if aMask in palindromes:
                        result = max(result, palindromes[mask] * palindromes[aMask])
        return result
        
# @lc code=end

