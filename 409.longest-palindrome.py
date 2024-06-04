#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    '''
    To build a palindrome, we need even number of occurences    
    '''
    def longestPalindrome(self, s: str) -> int:
        hash_table = {}
        for c in s: hash_table[c] = 1 + hash_table.get(c, 0)
        palindrome_length = 0
        for key in hash_table.keys():
            palindrome_length += hash_table[key] - hash_table[key] % 2
            hash_table[key] -= hash_table[key] - hash_table[key] % 2
        return palindrome_length + (1 if 1 in hash_table.values() else 0)
# @lc code=end

