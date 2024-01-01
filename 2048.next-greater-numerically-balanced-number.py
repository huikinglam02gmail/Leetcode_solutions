#
# @lc app=leetcode id=2048 lang=python3
#
# [2048] Next Greater Numerically Balanced Number
#

# @lc code=start
import bisect
from itertools import permutations


class Solution:
    '''
    0 <= n <= 10^6
    So we at most have 7 digits, and we can rule out using 7, 8 and 9. So what we need to do is to list out all the possible numbers, and sort them.
    '''
    def nextBeautifulNumber(self, n: int) -> int:
        parts = ["1", "22", "333", "4444", "55555", "666666"]
        possibilitiesLengths = [0] * (1 << 7)
        i = 0
        candidates = set()
        for mask in range(1, 1 << 6, 1):
            while mask >= (1 << i):
                i += 1
            possibilitiesLengths[mask] = possibilitiesLengths[mask - (1 << (i - 1))] + len(parts[i - 1])
            if 0 < possibilitiesLengths[mask] < 8:
                stringTemplate = ""
                for j in range(7):
                    if mask & (1 << j): stringTemplate += parts[j]
                stringPossibilities = permutations(stringTemplate, len(stringTemplate))
                for pos in stringPossibilities: candidates.add(int(''.join(pos)))
        vec = sorted(candidates)
        ind = bisect.bisect_right(sorted(candidates), n)
        return vec[ind]

# @lc code=end

