#
# @lc app=leetcode id=1016 lang=python3
#
# [1016] Binary String With Substrings Representing 1 To N
#

# @lc code=start
class Solution:
    '''
    First impression of the question suggests the check priorities should be from high n to low.
    1 <= n <= 10^9
    Think about it a little more, how long s need to be to cover [1 10^9]?
    It would be enormous, on the order of 10^8
    but in our case, 1 <= s.length <= 1000
    Therefore if we can just keep scanning from n downwards and report false if cannot find
    generating binary string of n is easy
    '''
    def queryString(self, s: str, n: int) -> bool:
        for i in range(n, 0,-1):
            if bin(i)[2:] not in s:
                return False
        return True
# @lc code=end

