/*
 * @lc app=leetcode id=2551 lang=cpp
 *
 * [2551] Put Marbles in Bags
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>
using std::accumulate;
using std::sort;
using std::vector;
class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        if (k == 1)
        {
            return (long long)0;
        }

        vector<long long> data{};
        for (int i = 0; i < weights.size() - 1; i++)
        {
            data.push_back((long long)(weights[i] + weights[i + 1]));
        }

        sort(data.begin(), data.end());
        return accumulate(data.end() - k + 1, data.end(), (long long)0) - accumulate(data.begin(), data.begin() + k - 1, (long long) 0);
    }
};
// @lc code=end

