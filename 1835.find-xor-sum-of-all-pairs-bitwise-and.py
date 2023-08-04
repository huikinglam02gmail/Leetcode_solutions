#
# @lc app=leetcode id=1835 lang=python3
#
# [1835] Find XOR Sum of All Pairs Bitwise AND
#

# @lc code=start
from typing import List


class Solution:
    '''
    In the final list, we are going to XOR 1 & 6 and 1 & 5 = (001 & 110) ^ (001 & 101). So consider for each digit: As 1 is 0 at 2^2 and 2^1, we know xoring  all the entries will have the 2nd and 1st digit as 0. For the 0th digit, we count the total of 1 in arr2: it is 1. So know (1 & 6) ^ (1 & 5) = 1. In general it will be sumi sumj(if arr1[j] & (1 << i) > 0 ) * (1 << i) * (cnts2[j] % 2))
    '''
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        numberOfDigits1 = max(arr1).bit_length()
        numberOfDigits2 = max(arr2).bit_length()
        numberOfDigits = max(numberOfDigits1, numberOfDigits2)

        if numberOfDigits1 > numberOfDigits2:
            arr1, arr2 = arr2, arr1
        cnts2 = [0]*numberOfDigits
        for num in arr2:
            for j in range(numberOfDigits):
                if num & (1 << j) > 0:
                    cnts2[j] += 1
        result = 0
        for num in arr1:
            for j in range(numberOfDigits):
                if num & (1 << j) > 0:
                    result ^= (1 << j) * (cnts2[j] % 2)
        return result

# @lc code=end

