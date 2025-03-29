#
# @lc app=leetcode id=2818 lang=python3
#
# [2818] Apply Operations to Maximize Score
#

# @lc code=start
import heapq
from typing import List


class Solution:
    '''
    First map the primes scores.
    Then we figure out for each primeScore, what are the first elements left and right of it which is larger than itself
    The number of sub arrays with nums[i] chosen as the element with highest prime score subArrayCount[i] = (i - lastGreater[i]) * (nextGreater[i] - i)
    To get the largest prime factor then the largest num, we use a max heap: [- nums[i], subArrayCount[i]]
    '''
    def maximumScore(self, nums: List[int], k: int) -> int:
        primeScores = []
        for num in nums: primeScores.append(len(self.primeFactors(num)))
        
        stack = []
        n = len(primeScores)
        nextGreater = [n for i in range(n)]
        lastGreater = [-1 for i in range(n)]
        for i in range(n):
            while stack and primeScores[i] > primeScores[stack[-1]]: nextGreater[stack.pop()] = i
            if stack: lastGreater[i] = stack[-1]
            stack.append(i)
        heap = []
        for i in range(n): heapq.heappush(heap, [- nums[i], (i - lastGreater[i]) * (nextGreater[i] - i)])

        MOD = 1000000007
        result = 1
        while k > 0 and heap:
            negNum, count =  heapq.heappop(heap)
            finalCount = min(k, count)
            result *= pow(- negNum, finalCount, MOD)
            result %= MOD
            k -= finalCount
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

