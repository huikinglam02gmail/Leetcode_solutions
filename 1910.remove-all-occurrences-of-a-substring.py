#
# @lc app=leetcode id=1910 lang=python3
#
# [1910] Remove All Occurrences of a Substring
#

# @lc code=start
class Solution:
    '''
    1 <= s.length <= 1000
    1 <= part.length <= 1000
    So just use stack
    '''
    def removeOccurrences(self, s: str, part: str) -> str:
        result = []
        n = len(part)
        for c in s:
            result.append(c)
            if len(result) >= n and ''.join(result[-n::]) == part:
                for j in range(n):
                    result.pop()
        return ''.join(result)

# @lc code=end

