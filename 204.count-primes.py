#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True]*n
        result = 0
        prime[0] = False
        prime[1] = False
        i = 2
        while i < n:
            if prime[i]:
                prime[i*i:n:i] = [False]*((n-1-i*i)//i + 1)
                result += 1
            i += 1
        return result
# @lc code=end

