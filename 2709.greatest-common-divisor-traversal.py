#
# @lc app=leetcode id=2709 lang=python3
#
# [2709] Greatest Common Divisor Traversal
#

# @lc code=start
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
    1 <= nums[i] <= 105
    Firstly, if nums contain 1, return false
    Otherwise, prime factorize num and put their indices to the prime numbers dict {prime : [indices]}
    Then use union find to union different indices within same prime
    Finally scan if all find(x) are the same
    '''
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        primeIndicesDict = {}
        for i in range(len(nums)):
            if nums[i] == 1: return False
            primeFacs = self.primeFactors(nums[i])
            for prime in primeFacs.keys():
                if prime not in primeIndicesDict: primeIndicesDict[prime] = []
                primeIndicesDict[prime].append(i)
        UF = UnionFindSet(len(nums))
        for prime, indices in primeIndicesDict.items():
            for i in range(1, len(indices), 1):
                UF.union(indices[0], indices[i])
        return UF.count == 1
    
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

