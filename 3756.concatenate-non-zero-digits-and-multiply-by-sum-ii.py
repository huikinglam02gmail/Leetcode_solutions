#
# @lc app=leetcode id=3756 lang=python3
#
# [3756] Concatenate Non-Zero Digits and Multiply by Sum II
#

# @lc code=start
import bisect
from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 1000000007
        cur = [0]
        prefix = [0]
        index = [-1]
        pow10 = [1]
        for i in range(len(s)):
            if s[i] == '0': continue
            cur.append((cur[-1] * 10 + int(s[i])) % MOD)
            prefix.append((prefix[-1] + int(s[i])) % MOD)
            index.append(i)
            pow10.append((pow10[-1] * 10) % MOD)
        res = []
        for l, r in queries:
            left = bisect.bisect_left(index, l)
            right = bisect.bisect_right(index, r) - 1
            x = cur[right] - cur[left - 1] * pow10[right - left + 1]
            x %= MOD
            sum = prefix[right] - prefix[left - 1]
            sum %= MOD
            res.append((x * sum) % MOD)
        return res
# @lc code=end

