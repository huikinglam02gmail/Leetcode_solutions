#
# @lc app=leetcode id=899 lang=python3
#
# [899] Orderly Queue
#

# @lc code=start
class Solution:
    # if k > 1: we can always swap anything two adjacent characters to achieve the whole string being lexicographically smallest
    # abc[XY]def -> bc[XY]defa -> c[XY]defab -> [XY]defabc -> XdefabcY -> defabc[YX] -> abc[YX]def
    # For k == 1: it's a rotation. Just compare all the possible
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        else:
            result = s
            for i in range(1,len(s)):
                if s[i:] + s[:i] < result:
                    result = s[i:] + s[:i]
            return result
# @lc code=end

