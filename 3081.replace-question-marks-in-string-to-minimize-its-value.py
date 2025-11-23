#
# @lc app=leetcode id=3081 lang=python3
#
# [3081] Replace Question Marks in String to Minimize Its Value
#

# @lc code=start
import heapq


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        counts = [0] * 26
        heap = []
        for c in s:
            if c != '?':
                counts[ord(c) - ord('a')] += 1
        for i in range(26):
            heapq.heappush(heap, [counts[i], chr(ord('a') + i)])
        temp = ""
        for c in s:
            if c == '?':
                count, char = heapq.heappop(heap)
                temp += char
                heapq.heappush(heap, [count + 1, char])
        temp = "".join(sorted([c for c in temp]))
        result = ""
        j = 0
        for c in s:
            if c != '?': result += c
            else:
                result += temp[j]
                j += 1
        return result


        
# @lc code=end
