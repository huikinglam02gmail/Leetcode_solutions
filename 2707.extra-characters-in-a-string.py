#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= s.length <= 50
    1 <= dictionary.length <= 50
    1 <= dictionary[i].length <= 50
    dp[i] =  minimum number of extra characters left over if you break up s[i:] optimally
    dp[i] = min(1 + dp[j] if s[i:j] is not inside dictionary;
                dp[j] if s[i:j] is inside dictionary)
    '''
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionarySet = set()
        for word in dictionary:
            dictionarySet.add(word)
        
        n = len(s)
        dp = [n] * (n + 1)
        dp[-1] = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1, 1):
                dp[i] = min(dp[i], j - i + dp[j] if s[i:j] not in dictionarySet else dp[j])
        return dp[0]
# @lc code=end

