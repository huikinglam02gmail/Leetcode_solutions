/*
 * @lc app=leetcode id=1883 lang=cpp
 *
 * [1883] Minimum Skips to Arrive at Meeting On Time
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <iostream>

using std::min;
using std::vector;

class Solution {
private:
    long long dpFunc(int i, int j) {
        if (j < 0) return LLONG_MAX;
        if (i == n) return (long long)0;
        if (dp[i][j] == (long long)(-1))
        {
            dp[i][j] = (long long)dist[i] + min(dpFunc(i + 1, j - 1), (long long)ceildiv(dpFunc(i + 1, j), speed) * (long long)speed);
        }
        return dp[i][j];
    }

    int ceildiv (int a, int b) {
        return (a + b - 1) / b;
    };

    vector<int> dist;
    int speed;
    int hoursBefore;
    int n;
    std::vector<vector<long long>> dp;

public:
    int minSkips(std::vector<int>& dist, int speed, int hoursBefore) {
        this->n = dist.size();
        this->dist = dist;
        this->speed = speed;
        this->hoursBefore = hoursBefore;

        dp = vector<vector<long long>>(n, vector<long long>(n, -1));
        long long S = (long long)0;
        for (int d : dist)
        {
            S += (long long)d;
        }
        if (S > (long long)speed * (long long)hoursBefore) {
            return -1;
        }

        for (int i = 0; i < n; i++) {
            if (dpFunc(0, i) <= (long long)speed * (long long)hoursBefore) {
                return i;
            }
        }

        return -1;
    }
};

// @lc code=end

