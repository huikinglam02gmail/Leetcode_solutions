#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
class Solution:
    '''
    Python program to print all primes smaller than or equal to n using Sieve of Eratosthenes
    '''
    def SieveOfEratosthenes(self, n):
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n + 1, p): prime[i] = False
            p += 1
        prime[0]= False
        prime[1]= False
        primes = []
        for p in range(n + 1):
            if prime[p]: primes.append(p)
        return primes

    '''
    Think about the situation
    If there are n = 10, how do we get 10 'A's?
    copy and paste 'A' to get 2 'A's (1 + 1)
    Then copy 'AA' and paste 4 times (1 + 4) -> 7
    Whether we do 'AAAAA' * 2 or 'AA' * 5 does not matter. 
    so this is about prime factorization
    Let's think about n == 12
    it is 2X2X3
    Copy and paste "A" = 2 steps
    Copy "AA"  and paste 5 times = 7 steps = 2 + 2 + 3
    Final example: n == 20
    it is 2X2X5
    result = 9 = 2 + 2 + 5
    so the ans is simple! just add the prime factors!    
    '''
    def minSteps(self, n: int) -> int:
        primes = self.SieveOfEratosthenes(n)
        factors = []
        index = 0
        while n > 1:
            if n % primes[index] > 0:
                index += 1
            else:
                factors.append(primes[index])
                n //= primes[index]
        return sum(factors)
        
# @lc code=end

