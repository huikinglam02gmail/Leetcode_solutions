#
# @lc app=leetcode id=3365 lang=python3
#
# [3365] Rearrange K Substrings to Form Target String
#

# @lc code=start
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        hashTableS = {}
        hashTableT = {}
        for i in range(k): hashTableS[s[i * (len(s) // k) : (i + 1) * (len(s) // k)]] = hashTableS.get(s[i * (len(s) // k) : (i + 1) * (len(s) // k)], 0) + 1
        for i in range(k): hashTableT[t[i * (len(t) // k) : (i + 1) * (len(t) // k)]] = hashTableT.get(t[i * (len(t) // k) : (i + 1) * (len(t) // k)], 0) + 1
        for key, val in hashTableS.items():
            if key not in hashTableT or hashTableT[key] != val: return False
        return True
# @lc code=end

