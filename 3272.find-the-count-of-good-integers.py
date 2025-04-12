#
# @lc app=leetcode id=3272 lang=python3
#
# [3272] Find the Count of Good Integers
#

# @lc code=start
class Solution:
    '''
    Construct the k-palindromes, and count combinations of good integers excluding ones with leading zero 
    '''
    def countGoodIntegers(self, n: int, k: int) -> int:
        base = pow(10, (n - 1) // 2)
        seen = {}
        for xHalf in range(base, 10* base):
            if n % 2 > 0: x = int(str(xHalf) + str(xHalf)[-2::-1])
            else: x = int(str(xHalf) + str(xHalf)[-1::-1])
            if x % k == 0:
                key = "".join(sorted(c for c in str(x)))
                if key not in seen: 
                    seen[key] = [0] * 10
                    for c in key: seen[key][ord(c) - ord('0')] += 1
        factorials = [1]
        for i in range(n): factorials.append(factorials[-1] * (i + 1))
        result = 0
        for key in seen:
            current = (n - seen[key][0]) * factorials[n - 1]
            for i in range(10): current //= factorials[seen[key][i]]
            result += current
        return result
# @lc code=end
