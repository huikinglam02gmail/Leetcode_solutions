#
# @lc app=leetcode id=2840 lang=python3
#
# [2840] Check if Strings Can be Made Equal With Operations II
#

# @lc code=start
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) == 1: return s1 == s2
        else:
            return "".join(sorted(c1 for c1 in s1[0::2])) == "".join(sorted(c2 for c2 in s2[0::2])) and "".join(sorted(c3 for c3 in s1[1::2])) == "".join(sorted(c4 for c4 in s2[1::2]))
# @lc code=end

