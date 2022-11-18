#
# @lc app=leetcode id=1471 lang=python3
#
# [1471] The k Strongest Values in an Array
#

# @lc code=start
import heapq


class Solution:
    # Find the median first
    # Then put all the elements into a max heap
    # with [-abs(value - median value), - index]
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arrSorted = sorted(arr)
        n = len(arr)
        median = arrSorted[(n-1)//2]
        heap = []
        for i, num in enumerate(arr):
            heapq.heappush(heap, [- abs(median - num), -arr[i]])
        result = []
        for i in range(k):
            diff, num = heapq.heappop(heap)
            result.append(-num)
        return result
# @lc code=end

