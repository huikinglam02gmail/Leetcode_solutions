#
# @lc app=leetcode id=2982 lang=python3
#
# [2982] Find Longest Special Substring That Occurs Thrice II
#

# @lc code=start
import heapq


class Solution:
    def maximumLength(self, s: str) -> int:
        longest = [[] for i in range(26)]
        count = 0
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]: count += 1
            else: count = 1
            if i == len(s) - 1 or s[i + 1] != s[i]:
                heapq.heappush(longest[ord(s[i]) - ord('a')], count)
                if count > 1: heapq.heappush(longest[ord(s[i]) - ord('a')], count - 1)
                if count > 2: heapq.heappush(longest[ord(s[i]) - ord('a')], count - 2)
                while len(longest[ord(s[i]) - ord('a')]) > 3: heapq.heappop(longest[ord(s[i]) - ord('a')])
        result = -1
        for heap in longest:
            if len(heap) >= 3:
                result = max(result, heapq.heappop(heap))
        return result
# @lc code=end

