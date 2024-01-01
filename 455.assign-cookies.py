#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List


class Solution:
    '''
    sort both first and try to assign cookies to whoever that would be content
    '''
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content = ps = 0
        while content < len(g) and ps < len(s):
            if s[ps] >= g[content]: content += 1
            ps += 1
        return content
# @lc code=end

