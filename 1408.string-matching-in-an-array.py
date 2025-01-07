#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#

# @lc code=start
from typing import List


class Solution:
    '''
    O(N^2) solutions should be acceptable, let's try!    
    '''
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x: len(x))
        n = len(words)
        result = set()
        for i in range(n-2, -1,-1):
            for j in range(i+1, n):
                if words[i] in words[j]:
                    result.add(words[i])
        return list(result)
        
# @lc code=end

