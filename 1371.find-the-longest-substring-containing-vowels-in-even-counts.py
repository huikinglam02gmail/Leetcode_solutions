#
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#

# @lc code=start
class Solution:
    '''
    We do not care about non vowels
    and there are only 5 vowels, aeiou
    And we do not care about the exact number, but only if they are odd or even.
    Therefore we might use a bitmask of length 5 to represent the vowels (even / odd)
    The number of possible states is only 32
    We can then iterate through s
    If we see non vowels, we simply attach the current index to the XOR key
    If we see vowels, we update the current key by applying ^ (1<<i)
    Afterwards, we can easily find the longest substring by subtracting the last index of x and first index of x^0    
    '''
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        vowels_map = {}
        for i, c in enumerate(vowels): vowels_map[c] = i
        
        hash_table, prefix = {}, 0
        hash_table[0] = [-1]
        for i, c in enumerate(s):
            if c in vowels: prefix ^= (1 << vowels_map[c])
            if prefix not in hash_table: hash_table[prefix] = []
            if len(hash_table[prefix]) <= 1: hash_table[prefix].append(i)
            else: hash_table[prefix][-1] = i
        
        result = 0
        for i in range(1 << 5):
            if i in hash_table and i^0 in hash_table: result = max(result, hash_table[i][-1]-hash_table[i^0][0])
        return result
# @lc code=end

