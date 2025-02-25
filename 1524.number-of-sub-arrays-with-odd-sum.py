#
# @lc app=leetcode id=1524 lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
#

# @lc code=start
from typing import List


class Solution:
    '''
    Just break down the problem more generally: what is the number of subarrays ending at index i with an odd and even sum?
    dp[i][0 vs 1]    
    '''
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even, n, result, MOD = 0, 0, len(arr), 0, pow(10,9) + 7
        for i in range(n):
            oddNew, evenNew = 0, 0
            if arr[i] % 2 == 1:
                oddNew += 1
                if i > 0:
                    oddNew += even
                    evenNew += odd
            else:
                evenNew += 1
                if i > 0:
                    oddNew += odd
                    evenNew += even
            odd, even = oddNew, evenNew
            result += odd
            result %= MOD
        return result 
# @lc code=end

