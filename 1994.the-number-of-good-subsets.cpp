/*
 * @lc app=leetcode id=1994 lang=cpp
 *
 * [1994] The Number of Good Subsets
 */

// @lc code=start
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int numberOfGoodSubsets(vector<int>& nums) {
        int primes[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };
        int count1 = 0;
        unordered_map<int, int> hashTable;

        for (int num : nums) {
            if (num == 1) {
                count1++;
            } else if (num % 4 > 0 && num % 9 > 0 && num % 25 > 0) {
                if (hashTable.find(num) != hashTable.end()) {
                    hashTable[num]++;
                } else {
                    hashTable[num] = 1;
                }
            }
        }

        vector<long long> dp(1 << 10, 0);
        dp[0] = 1;
        long long MOD = 1000000007;

        for (const auto& entry : hashTable) {
            int key = entry.first;
            int keyMask = 0;
            for (int i = 0; i < sizeof(primes) / sizeof(primes[0]); i++) {
                if (key % primes[i] == 0) {
                    keyMask |= 1 << i;
                }
            }

            for (int mask = (1 << 10) - 1; mask >= 0; mask--) {
                if ((mask & keyMask) == 0) {
                    dp[mask ^ keyMask] += entry.second * dp[mask];
                    dp[mask ^ keyMask] %= MOD;
                }
            }
        }

        return static_cast<int>((modPow(2, count1, MOD) * ((sum(dp) - 1) % MOD)) % MOD);
    }

private:
    long long modPow(long long x, long long y, long long m) {
        if (y == 0) return 1;
        long long p = modPow(x, y / 2, m);
        p = (p * p) % m;
        return y % 2 == 1 ? (p * (x % m)) % m : p;
    }

    long long sum(const vector<long long>& array) {
        long long sum = 0;
        for (long long num : array) {
            sum += num;
        }
        return sum;
    }
};

// @lc code=end

