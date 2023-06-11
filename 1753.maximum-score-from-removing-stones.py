#
# @lc app=leetcode id=1753 lang=python3
#
# [1753] Maximum Score From Removing Stones
#

# @lc code=start
import heapq


class Solution:
    '''
    The worst situation is you used up the smallest one and have a lot of unused in the largest ones. Therefore, Deplete the largest 2 first: x >= y >= z
    inside heap is [- x, - y, - z]
    we can get y to become z - 1: result += (y - z + 1)
    x -> x - (y - z + 1), y - > z - 1
    '''
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [- a, - b, - c]
        heapq.heapify(heap)
        result = 0
        while len(heap) >= 2:
            x = - heapq.heappop(heap)
            y = - heapq.heappop(heap)
            if len(heap) > 0:
                z = - heap[0]
                result += y - z + 1
                x -= (y - z + 1)
                y = z - 1
                if y > 0:
                    heapq.heappush(heap, - y)
                if x > 0:
                    heapq.heappush(heap, - x)
            else:
                result += y
        return result

# @lc code=end
