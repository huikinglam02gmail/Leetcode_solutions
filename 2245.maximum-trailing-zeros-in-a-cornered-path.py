#
# @lc app=leetcode id=2245 lang=python3
#
# [2245] Maximum Trailing Zeros in a Cornered Path
#

# @lc code=start
from typing import List


class Solution:
    '''
    1 <= grid[i][j] <= 1000
    So break down all numbers in the range into it's prime factorization.
    The number of trailing 0s is given by min(accumulated 2, accumulated 5)
    We can use prefix sum to denote how many 2 and 5 accumulated on horizontal and vertical paths  
    '''
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        primes = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in primes: 
                    primes[grid[i][j]] = self.primeFactors(grid[i][j])
        
        prefixHorizontal = []
        for i in range(len(grid)):
            prefixHorizontal.append([[0, 0]])
            twos, fives = 0, 0
            for j in range(len(grid[i])):
                twos += primes[grid[i][j]].get(2, 0)
                fives += primes[grid[i][j]].get(5, 0)
                prefixHorizontal[i].append([twos, fives])
        
        prefixVertical = []
        for j in range(len(grid[0])):
            prefixVertical.append([[0, 0]])
            twos, fives = 0, 0
            for i in range(len(grid)):
                twos += primes[grid[i][j]].get(2, 0)
                fives += primes[grid[i][j]].get(5, 0)
                prefixVertical[j].append([twos, fives])
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                twosLeft, fivesLeft = prefixHorizontal[i][j + 1]
                twosRight, fivesRight = prefixHorizontal[i][-1][0] - prefixHorizontal[i][j][0], prefixHorizontal[i][-1][1] - prefixHorizontal[i][j][1]
                twosUp, fivesUp = prefixVertical[j][i]
                twosDown, fivesDown = prefixVertical[j][-1][0] - prefixVertical[j][i + 1][0], prefixVertical[j][-1][1] - prefixVertical[j][i + 1][1]
                result = max(result, min(twosLeft + twosUp, fivesLeft + fivesUp))
                result = max(result, min(twosRight + twosUp, fivesRight + fivesUp))
                result = max(result, min(twosLeft + twosDown, fivesLeft + fivesDown))
                result = max(result, min(twosRight + twosDown, fivesRight + fivesDown))
        return result
                    
    '''
    A function to store the prime factor as key and power as value in a dictionay 
    '''
    def primeFactors(self, n):
        primes = {}
        while n % 2 == 0:
            primes[2] = primes.get(2, 0) + 1
            n //= 2

        i = 3
        while i * i <= n:
            while n % i == 0:
                primes[i] = primes.get(i, 0) + 1
                n //= i
            i += 2
        if n > 1:
            primes[n] = primes.get(n, 0) + 1
        return primes
# @lc code=end
