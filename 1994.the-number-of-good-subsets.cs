/*
 * @lc app=leetcode id=1994 lang=csharp
 *
 * [1994] The Number of Good Subsets
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int NumberOfGoodSubsets(int[] nums) {
        int[] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };
        int count1 = 0;
        Dictionary<int, int> hashTable = new Dictionary<int, int>();

        foreach (int num in nums) {
            if (num == 1) {
                count1++;
            } else if (num % 4 > 0 && num % 9 > 0 && num % 25 > 0) {
                if (hashTable.ContainsKey(num)) {
                    hashTable[num]++;
                } else {
                    hashTable[num] = 1;
                }
            }
        }

        long[] dp = new long[1 << 10];
        dp[0] = 1;
        long MOD = 1000000007;

        foreach (int key in hashTable.Keys) {
            int keyMask = 0;
            for (int i = 0; i < primes.Length; i++) {
                if (key % primes[i] == 0) {
                    keyMask |= 1 << i;
                }
            }

            for (int mask = (1 << 10) - 1; mask >= 0; mask--) {
                if ((mask & keyMask) == 0) {
                    dp[mask ^ keyMask] += hashTable[key] * dp[mask];
                    dp[mask ^ keyMask] %= MOD;
                }
            }
        }

        return (int)((ModPow(2, count1, MOD) * ((dp.Sum() - 1) % MOD)) % MOD);
    }

    public static long ModPow(long x, long y, long m) 
    {
        if (y == 0) return 1;
        long p = ModPow(x, y / 2, m);
        p = (p * p) % m;
        return y % 2 == 1 ? (p * (x % m)) % m : p;
    }
}

// @lc code=end

