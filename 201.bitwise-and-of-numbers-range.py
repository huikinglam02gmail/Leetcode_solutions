#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    '''
    Special case: same number
    otherwise:
    if left and right do not have the same count of bits to represent, for example left = 3, right = 8, the answer must be 0, because 1000 && 0011 must be 0
    if left and right share the same number of representing bits, e.g. left = 5 = 101, right = 7 = 111, we know every number between 5 and 7 must have the leftmost bit being 1, so the final answer must be at least 100 = 4
    '''

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right: return left
        else:
            left_count = 0
            temp = left
            while temp > 0:
                left_count += 1
                temp //= 2
            right_count = 0
            temp = right
            while temp > 0:
                right_count += 1
                temp //= 2
            if left_count != right_count:
                return 0
            else:
                left -= pow(2, left_count - 1)
                right -= pow(2, right_count - 1)
                return pow(2, left_count - 1) + self.rangeBitwiseAnd(left, right)
# @lc code=end

