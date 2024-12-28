#
# @lc app=leetcode id=2381 lang=python3
#
# [2381] Shifting Letters II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        heap = []
        for start, end, direction in shifts:
            dir = 1
            if direction == 0: dir = -1
            heapq.heappush(heap, [start, dir])
            heapq.heappush(heap, [end + 1, - dir])
        
        cur = 0
        result = ""
        for i in range(len(s)):
            while heap and heap[0][0] == i:
                ind, dir = heapq.heappop(heap)
                cur += dir
                if cur < 0: cur += 26   
            result += chr(ord('a') + (ord(s[i]) - ord('a') + cur) % 26)
        return result
# @lc code=end

