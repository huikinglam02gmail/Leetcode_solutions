#
# @lc app=leetcode id=2380 lang=python3
#
# [2380] Time Needed to Rearrange a Binary String
#

# @lc code=start
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        steps = 0
        count = len(s)
        while count > 0:
            count = 0
            i = 0
            sNew = ""
            while i < len(s):
                if i < len(s) - 1 and s[i] == "0" and s[i + 1] == "1":
                    count += 1
                    sNew += "10"
                    i += 2
                else:
                    sNew += s[i]
                    i += 1
            s = sNew
            if count > 0: steps += 1
        return steps
# @lc code=end

