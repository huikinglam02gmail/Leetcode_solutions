#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
class Solution:
    # The simulation approach is obvious
    # But we can use the property of prefix XOR to handle the problem
    # For example, we have 4^6^8^10 = (0^2^4^6^8^10)^(0^2)
    # And then we observe the property of 0^...^(2*n) = prefix_even(n)
    # if n % 4 == 0: prefix_even(n) = 2*n
    # if n % 4 == 1: prefix_even(n) = 2
    # if n % 4 == 2: prefix_even(n) = 2*n ^ 2
    # if n % 4 == 3: prefix_even(n) = 0
    # Now we check for 1^...^(2*n+1) = prefix_odd
    # if n % 4 == 0: prefix_odd(n) = 2*n + 1
    # if n % 4 == 1: prefix_odd(n) = 2
    # if n % 4 == 2: prefix_odd(n) = (2*n+1) ^ 2
    # if n % 4 == 3: prefix_odd(n) = 0

    def prefix(self, endNum):
        if endNum % 2 == 0:
            n = endNum // 2
        else:
            n = (endNum - 1) // 2
        if n % 4 == 0:
            return endNum
        elif n % 4 == 2:
            return endNum ^ 2
        elif n % 4 == 1:
            return 2
        else:
            return 0

    def xorOperation(self, n: int, start: int) -> int:
        end = start + 2*(n-1)
        if start > 1:
            return self.prefix(end) ^ self.prefix(start - 2)
        else:
            return self.prefix(end)
# @lc code=end

