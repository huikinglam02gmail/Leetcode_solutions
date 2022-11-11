#
# @lc app=leetcode id=1447 lang=python3
#
# [1447] Simplified Fractions
#

# @lc code=start
class Solution:
    # for each n > 1, we loop from 1 to n-1
    # simplify the fraction by dividing their gcd, and use hash set to save seens fractions
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        else:
            result = set()
            for i in range(2,n+1):
                for j in range(1,i):
                    result.add(str(j // self.gcd(i, j)) + '/' + str(i // self.gcd(i, j)))
            return list(result)
        
# @lc code=end

