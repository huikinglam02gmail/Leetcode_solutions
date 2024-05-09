/*
 * @lc app=leetcode id=3075 lang=cpp
 *
 * [3075] Maximize Happiness of Selected Children
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end());
        int n = happiness.size();
        long long result = 0;
        for (int i = n - 1; i >= n - k; i--) {
            result += max(0, happiness[i] - (n - 1 - i));
        }
        return result;
    }
};

// @lc code=end

