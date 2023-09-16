#
# @lc app=leetcode id=1898 lang=python3
#
# [1898] Maximum Number of Removable Characters
#

# @lc code=start
from typing import List


class Solution:
    '''
    Then binary search
    Use isSubsequence
    '''
    def isSubsequence(self, s: str, t: str, mid) -> bool:
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2] and (p2 not in self.reverseRemovable or self.reverseRemovable[p2] >= mid):
                p1 += 1
            p2 += 1
        return p1 == len(s)
    

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        l, r = 0, len(removable)
        self.reverseRemovable = {}
        for i in range(len(removable)):
            self.reverseRemovable[removable[i]] = i
        while l < r:
            mid = l + (r - l) // 2
            if self.isSubsequence(p, s, mid):
                l = mid + 1
            else:
                r = mid
        if l == len(removable) and self.isSubsequence(p, s, l):
            return l
        else:
            return l - 1

# @lc code=end

