#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
class Solution:
    # From 1 to sqrt(n), compute the factor list
    def kthFactor(self, n: int, k: int) -> int:
        i, factors = 1, set()
        while i*i <= n:
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
            i += 1
        factors = sorted(list(factors))
        if k > len(factors):
            return -1
        else:
            return factors[k-1]
        
# @lc code=end

