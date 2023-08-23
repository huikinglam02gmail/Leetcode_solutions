#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
import heapq


class Solution:   
    def reorganizeString(self, s: str) -> str:
        hash_table = [0]*26
        for c in s:
            hash_table[ord(c)-ord('a')] += 1
        if max(hash_table) > len(s) // 2 + len(s) % 2:
            return ""
        self.heap = []
        for i in range(26):
            if hash_table[i] > 0:
                heapq.heappush(self.heap, [- hash_table[i], chr(i + ord('a'))])
        
        result = ""
        while self.heap:
            negCount1, chr1 = heapq.heappop(self.heap)
            negCount1 += 1
            if self.heap:
                negCount2, chr2 = heapq.heappop(self.heap)
                if result and result[-1] == chr1:
                    result += chr2
                    negCount2 += 1
                if negCount2 < 0:
                    heapq.heappush(self.heap, [negCount2, chr2])
            result += chr1
            if negCount1 < 0:
                heapq.heappush(self.heap, [negCount1, chr1])
        return result
# @lc code=end

