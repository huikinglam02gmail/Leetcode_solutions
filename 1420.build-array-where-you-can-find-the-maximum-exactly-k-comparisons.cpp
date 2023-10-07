/*
 * @lc app=leetcode id=1420 lang=cpp
 *
 * [1420] Build Array Where You Can Find The Maximum Exactly K Comparisons
 */

// @lc code=start
#include <vector>
#include <map>
#include <tuple>

class Solution {
public:
    const long long MOD = 1000000007;
    std::map<std::tuple<int, int, int>, long long> memo;

    long long dp(int i, int j, int l) {
        std::tuple<int, int, int> key = std::make_tuple(i, j, l);
        if (memo.find(key) != memo.end()) {
            return memo[key];
        }
        else {
            long long result = 0;
            if (i == 1 && l == 1) {
                result += 1;
            }
            else if (i > 1) {
                result += (j * dp(i - 1, j, l)) % MOD;
                result %= MOD;
                if (l > 1) {
                    for (int x = 1; x < j; x++) {
                        result += dp(i - 1, x, l - 1) % MOD;
                        result %= MOD;
                    }
                }
            }
            memo[key] = result;
            return result;
        }
    }

    int numOfArrays(int n, int m, int k) {
        long long final = 0;
        for (int i = 1; i <= m; i++) {
            final += dp(n, i, k) % MOD;
            final %= MOD;
        }
        return static_cast<int>(final);
    }
};

// @lc code=end

