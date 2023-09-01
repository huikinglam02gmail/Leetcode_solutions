#
# @lc app=leetcode id=1881 lang=python3
#
# [1881] Maximum Value after Insertion
#

# @lc code=start
class Solution:
    '''
    Key is to find the sign
    if positive, insert at the first instance which we see a smaller digit
    if negative, insert at the first instance which we see a larger digit
    '''
    def maxValue(self, n: str, x: int) -> str:
        neg = n[0] == "-"
        i = 0
        i = 1 if neg else 0
        stop = False
        while i < len(n) and not stop:
            if neg:
                stop = x < int(n[i])
            else:
                stop = x > int(n[i])
            if not stop:
                i += 1
        return n[:i] + str(x) + n[i:]
# @lc code=end

