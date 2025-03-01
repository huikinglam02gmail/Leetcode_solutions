#
# @lc app=leetcode id=3442 lang=python3
#
# [3442] Maximum Difference Between Even and Odd Frequency I
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str) -> int:
        count = [0] * 26
        for c in s: count[ord(c) - ord('a')] += 1
        parity = [[] for i in range(2)]
        for i in range(26): 
            if count[i] > 0: parity[count[i] % 2].append(count[i])
        for i in range(2): parity[i].sort()
        return parity[1][-1] - parity[0][0]
# @lc code=end

