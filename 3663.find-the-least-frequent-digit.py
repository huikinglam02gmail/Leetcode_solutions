#
# @lc app=leetcode id=3663 lang=python3
#
# [3663] Find The Least Frequent Digit
#

# @lc code=start
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        counts = [0] * 10
        while n > 0:
            digit = n % 10
            counts[digit] += 1
            n //= 10
        data = [[count, digit] for digit, count in enumerate(counts) if count > 0]
        data.sort()
        return data[0][1]
# @lc code=end

