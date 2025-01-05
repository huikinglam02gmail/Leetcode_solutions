#
# @lc app=leetcode id=2271 lang=python3
#
# [2271] Maximum White Tiles Covered by a Carpet
#

# @lc code=start
import bisect
from operator import itemgetter
from typing import List


class Solution:
    '''
    1 <= li <= ri <= 10^9
    1 <= carpetLen <= 10^9
    1 <= tiles.length <= 5 * 10^4
    we first sort tiles.
    It's always better to start the carpet from tiles[i][0] because we know we must lose the carpet length before it if placed otherwise.
    To find the maximum covered tiles, we prepare a prefix sum array                                                                                                                                                                                
    '''
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        newTiles = []
        for a, b in tiles:
            if newTiles and a == newTiles[-1][1] + 1: newTiles[-1][1] = b
            else: newTiles.append([a, b])
        prefix = [[-1, 0, -1]]
        for a, b in newTiles:
            prefix.append([a - 1, prefix[-1][1], -2])
            prefix.append([a, prefix[-1][1] + 1, 1])
            prefix.append([b, prefix[-1][1] + b - a, 2])
            prefix.append([b + 1, prefix[-1][1], -1])
        result = 0
        for a, b in newTiles:
            aInd = bisect.bisect_left(prefix, a - 1, key=itemgetter(0))
            endInd = bisect.bisect_left(prefix, a + carpetLen - 1, key=itemgetter(0))
            beginCount = prefix[aInd][1]
            if endInd == len(prefix): endInd -= 1
            endCount = prefix[endInd][1]
            if prefix[endInd][2] == 2: endCount -= prefix[endInd][0] - (a + carpetLen - 1)
            result = max(result, endCount - beginCount)
        return result
# @lc code=end
