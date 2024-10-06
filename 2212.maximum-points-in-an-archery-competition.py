#
# @lc app=leetcode id=2212 lang=python3
#
# [2212] Maximum Points in an Archery Competition
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each sector, as it's either Alice or Bob wins, we can use a bit mask to represent whether Bob won the sector
    We also save final score for each bitMask: scoreMask[mask] = mask
    If smaller than numArrows, we can add the difference into one of the set bits
    '''
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        minArrows = [-1 for i in range(1 << 12)]
        minArrows[0] = 0
        scoreMask = [0 for i in range(1 << 12)]
        for bit in range(12):
            for mask in range((1 << bit), 1 << (bit + 1), 1):
                scoreMask[mask] = bit + scoreMask[mask - (1 << bit)]
                minArrows[mask] = minArrows[mask - (1 << bit)] + aliceArrows[bit] + 1
        data = []
        for mask in range(1 << 12):
            if minArrows[mask] <= numArrows:
                data.append([scoreMask[mask], mask])
        data.sort(key = lambda x: -x[0])
        result = [0] * 12
        if data:
            seenLastSetBit = False
            for i in range(12):
                if data[0][1] & (1 << i) > 0:
                    result[i] = aliceArrows[i] + 1
                    if not seenLastSetBit:
                        seenLastSetBit = True
                        result[i] += numArrows - minArrows[data[0][1]]
        return result

# @lc code=end

