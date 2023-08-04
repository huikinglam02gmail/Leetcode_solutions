#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    '''
    Try breaking down the word bit by bit
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        seen = set()
        seen.add(s)
        while q:
            s = q.popleft()
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False
# @lc code=end

