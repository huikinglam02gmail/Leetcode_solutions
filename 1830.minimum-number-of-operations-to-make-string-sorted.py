#
# @lc app=leetcode id=1830 lang=python3
#
# [1830] Minimum Number of Operations to Make String Sorted
#

# @lc code=start
class Solution:
    '''
    From Example 1, we should see that the procedure described gives the previous permutation. So the question is how many lexicographically smaller string with same set of characters exist under s
    To do that, take a simple example: s = "cabbcdba". Consider from left to right
    Any string started with a or b will be smaller than s. So the first position has 5 possibilities: 2 a + 3 b, and the rest 7 positions we are free to choose. For number of combinations it would be ('a' chosen for 1st character) 7! / 1! / 3! / 2! / 1! + ('b' chosen for 1st character) 7! / 2! / 2! / 2! / 1! = 5 * 7! / 2! / 3! / 2! / 1! = sum(count(character smaller than current character) * (n - 1 - i)! / (product of count[i]!))
    To get the (1 / k!) % MOD, we use the fact that MOD is prime and Fermat's little theorem: (q ^ MOD) mod (MOD) = q mod (MOD). Therefore (1 / q) mod (MOD) = (q ^ (MOD - 2)) mod (MOD) 
    '''
    def makeStringSorted(self, s: str) -> int:
        MOD = pow(10, 9) + 7
        n = len(s)
        factorials = [1] * (n + 1)
        for i in range(1, n + 1):
            factorials[i] = factorials[i - 1] * i
            factorials[i] %= MOD

        inv = [1] * (n + 1)
        for i in range(1, n + 1):
            inv[i] = pow(factorials[i], MOD - 2, MOD)

        result = 0
        cnts = [0] * 26
        for i in range(n - 1, -1, -1):
            ind = ord(s[i]) - ord('a')
            cnts[ind] += 1
            current = sum(cnts[:ind])
            current *= factorials[n - 1 - i]
            current %= MOD
            for j in range(26):
                current *= inv[cnts[j]]
                current %= MOD
            result += current
            result %= MOD
        return result
        
# @lc code=end

