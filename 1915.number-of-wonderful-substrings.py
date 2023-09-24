#
# @lc app=leetcode id=1915 lang=python3
#
# [1915] Number of Wonderful Substrings
#

# @lc code=start
class Solution:
    '''
    We don't care about how many exact occurrence of each character before it, we only care about the number of odd / even occurence in substrings before it. Therefore we can use bitmask of 0 to represent even occurrence and 1 to represent odd occurrence. 
    Let's record dp[i][mask] = number of strings word[:j] for j = 0,..., i + 1 with odd and even appearance of each character represented by mask
    When we are given s[i], we know how many substrings between word[j:i + 1] would satisfy having 0 or 1 odd occurrence because we know then word[:j] would satisfy mask = current mask ^ (1 << i) or current mask
    '''
    def wonderfulSubstrings(self, word: str) -> int:
        current = 0
        dp = [1] + [0] * (1 << 10)
        result = 0
        for c in word:
            current ^= (1 << (ord(c) - ord('a')))
            result += dp[current]
            for i in range(10):
                result += dp[current ^ (1 << i)]
            dp[current] += 1
        return result

            
# @lc code=end

