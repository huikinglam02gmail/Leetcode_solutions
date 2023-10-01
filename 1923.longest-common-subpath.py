#
# @lc app=leetcode id=1923 lang=python3
#
# [1923] Longest Common Subpath
#

# @lc code=start
from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, ps: List[List[int]]) -> int:
        ps.sort(key=lambda x: len(x))
        l = 1
        r = len(ps[0]) + 1
        base_value = 100001
        mod = 100000000019

        while l < r:
            m = l + (r - l) // 2
            hs = set()

            for i in range(len(ps)):
                hash_val = 0
                d = 1
                hs1 = set()

                for j in range(len(ps[i])):
                    hash_val = (hash_val * base_value + ps[i][j]) % mod

                    if j >= m:
                        hash_val = (mod + hash_val - (d * ps[i][j - m]) % mod) % mod
                    else:
                        d = (d * base_value) % mod

                    if j >= m - 1 and (i == 0 or hash_val in hs):
                        hs1.add(hash_val)

                hs = hs1

            if not hs:
                r = m
            else:
                l = m + 1

        return l - 1


# @lc code=end

