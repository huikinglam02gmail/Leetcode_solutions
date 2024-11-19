#
# @lc app=leetcode id=3226 lang=python3
#
# [3226] Number of Bit Changes to Make Two Integers Equal
#

# @lc code=start
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        nBin = bin(n)[2:]
        kBin = bin(k)[2:]
        l = max(len(nBin), len(kBin))
        nBin = nBin.zfill(l)
        kBin = kBin.zfill(l)
        result = 0
        for i in range(l):
            if nBin[i] == '1' and kBin[i] == '0': result += 1
            elif nBin[i] == '0' and kBin[i] == '1': return -1
        return result
# @lc code=end

