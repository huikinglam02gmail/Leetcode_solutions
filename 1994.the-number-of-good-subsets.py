#
# @lc app=leetcode id=1994 lang=python3
#
# [1994] The Number of Good Subsets
#

# @lc code=start
from typing import List


class Solution:
    '''
    What can be used to form good subsets?
    1: we can put from 0 to all 1s to form a good subset. So basically if we collect all the non 1s, the answer will be 2 ^ count(1) * ans(nums[excluding 1])
    2. As 1 <= nums[i] <= 30, we first get all the primes under 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29].
    3. Then we test numbers from 2 to 30 whether they can be divided by 2 * 2, 3 * 3, 5 * 5
    4. Then we have a list of potential members to be used to form good subset. Then for each member, we assign bitmask to it according to the prime factorization. Each factor can only appear 1 or 0 times.
    5. After sorting the potential members (keys), we use a DP approach:
    dp[i][mask] = number of good subset with product represented by prime mask if we only consider keys[:i+1]
    dp[i][mask] = sum (dp[i - 1][mask ^ mask(keys[i])])) * count(keys[i]) if mask & mask(keys[i]) == 0
    Note the new dp values should
    '''

    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]      
        count1 = 0
        hashTable = {}
        for num in nums:
            if num == 1:
                count1 += 1
            elif num % 4 > 0 and num % 9 > 0 and num % 25 > 0:
                hashTable[num] = hashTable.get(num, 0) + 1
        
        dp = [0] * (1 << 10)
        dp[0] = 1
        MOD = pow(10, 9) + 7
        for key in hashTable.keys():
            keyMask = sum([(1 << i) for i, p in enumerate(primes) if key % p == 0])
            for mask in range((1 << 10) - 1, -1 , -1):
                if (mask & keyMask) == 0:
                    dp[mask ^ keyMask] += hashTable[key] * dp[mask]
                    dp[mask ^ keyMask] %= MOD
        return (pow(2, count1, MOD) * (sum(dp) - 1) % MOD) % MOD

# @lc code=end

