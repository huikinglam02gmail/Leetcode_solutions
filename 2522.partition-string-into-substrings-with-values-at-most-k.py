#
# @lc app=leetcode id=2522 lang=python3
#
# [2522] Partition String Into Substrings With Values at Most K
#

# @lc code=start
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        current = 0
        result = 0
        for c in s:
            if int(c) > k: return -1
            if current * 10 + int(c) > k:
                result += 1
                current = 0
            current *= 10
            current += int(c)
        return result + 1
# @lc code=end
