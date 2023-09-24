/*
 * @lc app=leetcode id=1915 lang=cpp
 *
 * [1915] Number of Wonderful Substrings
 */

// @lc code=start
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    long long wonderfulSubstrings(string word) {
        long long current = 0;
        vector<long long> dp(1 << 10, 0);
        dp[0] = 1;
        long long result = 0;

        for (char c : word) {
            current ^= (1LL << (c - 'a'));
            result += dp[current];

            for (int i = 0; i < 10; i++) {
                result += dp[current ^ (1LL << i)];
            }

            dp[current]++;
        }

        return result;
    }
};

// @lc code=end

