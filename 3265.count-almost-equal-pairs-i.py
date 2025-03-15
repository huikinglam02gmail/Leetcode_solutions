#
# @lc app=leetcode id=3265 lang=python3
#
# [3265] Count Almost Equal Pairs I
#

# @lc code=start
from typing import List


class Solution:
    '''
    For each num, generate its possible permutations
    At the same time keep track of the occurrence
    '''
    def countPairs(self, nums: List[int]) -> int:
        occur = {}
        variants = {}
        for num in nums:
            numString = str(num).zfill(7)
            if num not in variants:
                variants[num] = set()
                variants[num].add(num)
                for i in range(6):
                    for j in range(i + 1, 7):
                        numStringNew = numString[:i] + numString[j] + numString[i+1:j] + numString[i] + numString[j + 1:]
                        variants[num].add(int(numStringNew))
            occur[num] = occur.get(num, 0) + 1
        
        result = 0
        for num in occur:
            for num1 in variants[num]:
                if num == num1: result += occur.get(num, 0) * (occur.get(num, 0) - 1)
                else: result += occur.get(num, 0) * occur.get(num1, 0)
        return result // 2
# @lc code=end

