#
# @lc app=leetcode id=2063 lang=python3
#
# [2063] Vowels of All Substrings
#

# @lc code=start
class Solution:
    '''
    A dp problem
    dp[i] =  sum of the number of vowels in every substrings of word ending at i
    We want to get sum(dp)
    dp[i] = 
    1. if word[i] is vowel: 1 + dp[i - 1] + i
    2. else: dp[i - 1]
    '''
    def countVowels(self, word: str) -> int:
        last = 0
        result = 0
        n = len(word)
        for i in range(n):
            if word[i] in 'aeiou': last += i + 1
            result += last
        return result
# @lc code=end

