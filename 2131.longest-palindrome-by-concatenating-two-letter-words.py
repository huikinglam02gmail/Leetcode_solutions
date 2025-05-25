#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#

# @lc code=start
from typing import List


class Solution:
    '''
    all words are of length 2, so only 2 possibilities
    "XX", itself, can always be used even times. Only one odd extra might be inserted in the middle
    "XY" and "YX" pairs: minimum of them    
    '''
    def longestPalindrome(self, words: List[str]) -> int:
        hashTable = {}
        for word in words: hashTable[word] = hashTable.get(word, 0) + 1
        result = 0
        oddRepeat = False
        for key in hashTable:
            if key[0] == key[1]: 
                result += hashTable[key] // 2 * 4
                if hashTable[key] % 2 == 1: oddRepeat = True
            elif key[0] < key[1]:
                result += min(hashTable[key], hashTable.get(key[1] + key[0], 0)) * 4
        if oddRepeat: result += 2
        return result
        

# @lc code=end

