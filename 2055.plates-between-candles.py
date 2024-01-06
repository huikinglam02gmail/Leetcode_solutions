#
# @lc app=leetcode id=2055 lang=python3
#
# [2055] Plates Between Candles
#

# @lc code=start
import bisect
from operator import itemgetter
from typing import List


class Solution:
    '''
    First record indices of each candle and number of plates left of the candle.
    Then for each query we are interested in the first candle right of query[0] and last candle left of query[1]
    '''
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        plateCount = 0
        for i, c in enumerate(s):
            if c == '*': plateCount += 1
            else: candles.append([i, plateCount])
        result = []
        for l, r in queries:
            leftCandleIndex = bisect.bisect_left(candles, l, key=itemgetter(0))
            rightCandleIndex = bisect.bisect_right(candles, r, key=itemgetter(0)) - 1
            current = 0
            if leftCandleIndex < len(candles): current -= candles[leftCandleIndex][1]
            else: current -= plateCount
            if rightCandleIndex >= 0: current += candles[rightCandleIndex][1]
            result.append(max(current, 0))
        return result
# @lc code=end

