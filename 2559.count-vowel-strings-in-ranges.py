#
# @lc app=leetcode id=2559 lang=python3
#
# [2559] Count Vowel Strings in Ranges
#

# @lc code=start
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        beginEnd = []
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou": beginEnd.append(1)
            else: beginEnd.append(0)
        prefix = [0]
        for item in beginEnd:
            prefix.append(prefix[-1] + item)    
        result = []
        for start, end in queries: result.append(prefix[end + 1] - prefix[start])
        return result
# @lc code=end

