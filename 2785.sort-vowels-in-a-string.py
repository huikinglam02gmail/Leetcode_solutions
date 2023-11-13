#
# @lc app=leetcode id=2785 lang=python3
#
# [2785] Sort Vowels in a String
#

# @lc code=start
class Solution:
    '''
    Get all the vowels and their position. Sort the vowels and reassign to the new string.
    '''
    def sortVowels(self, s: str) -> str:
        vowels = []
        indices = []
        result = []
        for i, c in enumerate(s):
            if c in 'aeiouAEIOU':
                vowels.append(c)
                indices.append(i)
            result.append(c)
        
        vowels.sort(key = lambda x: ord(x))
        n = len(vowels)
        for i in range(n):
            result[indices[i]] = vowels[i]
        return "".join(result)
# @lc code=end

