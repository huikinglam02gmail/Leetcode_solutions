#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

# @lc code=start
from typing import List


class Solution:
    '''
    Build 26 character hash table for all words in words2
    Then get the max of all characters for each word
    Then for each word in words1, we check if the hash count are all larger or equal to that the words2 hash table    
    '''
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hash_words2 = [0]*26
        for word in words2:
            temp = [0]*26
            for c in word: temp[ord(c)-ord('a')] += 1
            for i in range(26): hash_words2[i] = max(hash_words2[i], temp[i])
        
        universal = []
        for word in words1:
            temp = [0]*26
            for c in word: temp[ord(c)-ord('a')] += 1
            isuniversal = True
            for i in range(26):
                if hash_words2[i] > 0 and temp[i] < hash_words2[i]: isuniversal = False
            if isuniversal: universal.append(word)
        return universal
# @lc code=end

