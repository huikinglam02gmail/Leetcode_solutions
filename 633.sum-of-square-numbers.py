#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        # binary search
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid*mid < x:
                left = mid + 1
            elif mid*mid > x:
                right = mid - 1
            else:
                return mid
        return left
    
    def judgeSquareSum(self, c: int) -> bool:
        # start with a = 0  b = sqrt(c) + 1
        a , b = 0, self.mySqrt(c) + 1
        while a <= b:
            if a*a + b*b < c:
                a += 1
            elif a*a + b*b > c:
                b -= 1
            else:
                return True
        return False
# @lc code=end

