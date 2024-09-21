#
# @lc app=leetcode id=2165 lang=python3
#
# [2165] Smallest Value of the Rearranged Number
#

# @lc code=start
class Solution:
    '''
    3 cases:
    1. 0: return 0
    2. > 0: sort the digits, find first nonnegative digit, pull it at front
    3. < 0: reverse sort the digits of - num
    '''
    def smallestNumber(self, num: int) -> int:
        if num == 0: return 0
        elif num > 0:
            result = []
            for c in str(num): result.append(c)
            result.sort()
            i = 0
            while i < len(result) and result[i] == '0': i += 1
            result[0], result[i] = result[i], result[0]
            return int("".join(result))
        else:
            return - int("".join(sorted([c for c in str(- num)], reverse=True)))
# @lc code=end

