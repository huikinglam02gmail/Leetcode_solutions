#
# @lc app=leetcode id=3541 lang=python3
#
# [3541] Find Most Frequent Vowel and Consonant
#

# @lc code=start
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        vowelFreq = {}
        consonantFreq = {}
        for char in s:
            if char in vowels: vowelFreq[char] = vowelFreq.get(char, 0) + 1
            else: consonantFreq[char] = consonantFreq.get(char, 0) + 1
        maxVowel = max(vowelFreq.values(), default=0)
        maxConsonant = max(consonantFreq.values(), default=0)
        return maxVowel + maxConsonant
# @lc code=end

