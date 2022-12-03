#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    # Zeroth condition: length must be the same
    # First condition: a character must be present in both word1 and word2
    # Second condition: free to swap frequencies under each character, so sort the value counts and check if they are the same
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False      
        occur1, occur2 = [0]*26, [0]*26
        for i in range(len(word1)):
            occur1[ord(word1[i]) - ord('a')] += 1
            occur2[ord(word2[i]) - ord('a')] += 1
        for i in range(26):
            if (occur1[i] == 0 and occur2[i] > 0) or (occur1[i] > 0 and occur2[i] == 0):
                return False
        occur1.sort()
        occur2.sort()        
        return all([occur1[i] == occur2[i] for i in range(26)])
        # @lc code=end

