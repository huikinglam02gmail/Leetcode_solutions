#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#

# @lc code=start
class Solution:
    # Odd number array
    # if even Length n, final target is (1 + 2*(n - 1) + 1) // 2 = n
    # if odd length n, final target is 2*(n//2) + 1
    # Then the answer is the arithmetic progression sum
    # if even n: ans = (1 + 2*(n-1) + 1 - n)*(n // 2) // 2= n*(n//2)//2
    # if odd n: ans = (2 + 2*(n-1) + 1 - n)*(n//2)//2 = (n+1)*(n//2)//2
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return n * (n // 2) // 2
        else:
            return (n + 1) * (n // 2) // 2
# @lc code=end

