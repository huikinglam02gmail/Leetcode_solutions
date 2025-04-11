#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for i in range(low, high + 1, 1):
            n = len(str(i))
            if n % 2 == 0:
                s = str(i)
                if sum([int(c) for c in s[: (n // 2)]]) == sum([int(c) for c in s[(n // 2):]]): result += 1
        return result
# @lc code=end

