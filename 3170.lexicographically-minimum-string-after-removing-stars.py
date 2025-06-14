#
# @lc app=leetcode id=3170 lang=python3
#
# [3170] Lexicographically Minimum String After Removing Stars
#

# @lc code=start
import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for i, c in enumerate(s):
            if c == '*': heapq.heappop(heap)
            else: heapq.heappush(heap, (c, -i))
        final = []
        while heap:
            c, negI = heapq.heappop(heap)
            final.append((-negI, c))
        final.sort()
        return ''.join(c for _, c in final)
# @lc code=end

