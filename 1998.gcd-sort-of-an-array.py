#
# @lc app=leetcode id=1998 lang=python3
#
# [1998] GCD Sort of an Array
#

# @lc code=start
from functools import lru_cache
from typing import List

class UnionFindSet:
    def __init__(self, n=0):
        self.parents = [i for i in range(n)]
        self.count = n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            pMax, pMin = max(pu,pv), min(pu,pv)
            self.parents[pMax] = pMin
            self.count -= 1

class Solution:
    '''
    gcd(a, b) > 1: a, b are not coprime.
    2 <= nums[i] <= 10^5: so get all the primes under max(nums), there is 9592 of them if the largest number is nums[i]
    To avoid wasting time to loop through these many primes, we instead could record the smallest prime factor of all numbers below max(nums)
    To do that, we used a modified version of Sieve of Eratosthenes: instead of recording whether a number if a prime or not, we record its smallest divisible prime
    We use union find to link up numbers which are not coprime by going through the sieve, to link the first detected node with all later detected node.
    We finally sort nums and compare with nums, to see if for each index i, nums[i] and sortedNums[i] belong to the same group
    '''
    
    '''
    Python program to return smallest prime divisor smaller than or equal to n using Sieve of Eratosthenes 
    '''  
    def smallestPrimeSieveOfEratosthenes(self, n): 
        prime = [i for i in range(n + 1)] 
        p = 2
        while (p * p <= n): 
            if (prime[p] == p):     
                for i in range(p * p, n + 1, p):
                    if prime[i] == i: prime[i] = p
            p += 1
        return prime
    
    @lru_cache(None)
    def allPrimeFactors(self, num): 
        if num <= 1: return set()
        p = self.smallestPrimes[num]
        if p == num: 
            return set([num])
        else:
            z = set([p]).union(self.allPrimeFactors(num // p))
            return z
    
    def gcdSort(self, nums: List[int]) -> bool:
        maxNum, n = max(nums), len(nums)
        self.smallestPrimes = self.smallestPrimeSieveOfEratosthenes(maxNum)
        primeToIndexDict = {}
        for i, num in enumerate(nums):
            primes = self.allPrimeFactors(num)
            for prime in primes:
                if prime not in primeToIndexDict:
                    primeToIndexDict[prime] = []
                primeToIndexDict[prime].append(i)

        UF = UnionFindSet(n)
        for p in primeToIndexDict:
            for i in range(1, len(primeToIndexDict[p])):
                UF.union(primeToIndexDict[p][0], primeToIndexDict[p][i])

        numSortedWithIndex = [[num, i] for i, num in enumerate(nums)]
        numSortedWithIndex.sort()

        for i in range(n):
            if UF.find(numSortedWithIndex[i][1]) != UF.find(i):
                return False
        return True
        
# @lc code=end

