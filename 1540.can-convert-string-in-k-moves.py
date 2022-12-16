#
# @lc app=leetcode id=1540 lang=python3
#
# [1540] Can Convert String in K Moves
#

# @lc code=start
class Solution:
    # lengths of s and t must be equal
    # Then for each position i we find the number of shift from s[i] to t[i]. It must be smaller than 26
    # The from 1 to 26 we ask if k // 26 >= the count
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        counts = [0]*26
        n = len(s)
        for i in range(n):
            counts[(ord(t[i]) + 26 - ord(s[i])) % 26] += 1
        for i in range(1, 26):
            if counts[i] > 0:
                if k // 26 + 1 < counts[i]:
                    return False
                elif k // 26 + 1 == counts[i] and k % 26 < i:
                    return False
        return True
# @lc code=end

