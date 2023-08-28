#
# @lc app=leetcode id=2801 lang=python3
#
# [2801] Count Stepping Numbers in Range
#

# @lc code=start
from functools import lru_cache


class Solution:
    '''
    Whenever we see "find number of something between a range [low, high]", we can reduce it to number of something between [1, high] - number of something between [1, low - 1].
    We notice for a number like "12345". Any stepping number starting with "0" would suffice. But leading zero is a special case: the digit following it can be anything from 0 to 9
    In here dp(i, tight, lastDigit) = number of stepping number if num[i:] is left behind, and whether we have a tight coherence to num before it, and the last digit of the stepping number. In here, -1 is used to denote leading zero.
    '''
    MOD = pow(10, 9) + 7
    def _count(self, num: str) -> int:
        @lru_cache(None)
        def dp(i, tight, lastDigit):
            if i == len(num): # whole num is processed
                return 1
            maxDigit = int(num[i]) if tight else 9 # if the previous processed numbers are tight, we can DP up to int(num[i]); otherwise it's 9.
            ans = 0
            
            for d in range(maxDigit + 1):
                nxtTight = tight and d == maxDigit # keep being tight if and only if the current digit is the maxDigit)
                if lastDigit == -1: # previous nums are leading zeroes
                    d = -1 if d == 0 else d # keep being leading zeros or else
                    ans += dp(i + 1, nxtTight, d)
                    ans += self.MOD
                elif abs(lastDigit - d) == 1: # stepping number; notice if lastDigit == maxDigit, it cannot go above; Also d cannot be negative
                    ans += dp(i + 1, nxtTight, d)
                    ans %= self.MOD
            return ans
        return dp(0, True, -1)

    def _minusOne(self, s):
        arr = [int(c) for c in s]
        carry = 1
        for i in range(len(arr) - 1, -1, -1):
            arr[i] -= carry
            carry = 0
            if arr[i] < 0:
                arr[i] += 10
                carry += 1
        i = 0
        while i < len(arr) and arr[i] == 0:
            i += 1
        result = "".join([str(num) for num in arr])
        return result[i:]

    def countSteppingNumbers(self, low: str, high: str) -> int:
        return (self._count(high) - self._count(self._minusOne(low)) + self.MOD) % self.MOD
# @lc code=end

