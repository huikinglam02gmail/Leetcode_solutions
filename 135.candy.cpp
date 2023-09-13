/*
 * @lc app=leetcode id=135 lang=cpp
 *
 * [135] Candy
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int candy(std::vector<int>& ratings) {
        int n = ratings.size();
        std::vector<int> result(n, 1);

        for (int i = 0; i < n - 1; i++) {
            if (ratings[i + 1] > ratings[i] && result[i + 1] <= result[i]) {
                result[i + 1] = result[i] + 1;
            }
        }

        for (int i = n - 1; i > 0; i--) {
            if (ratings[i] < ratings[i - 1] && result[i] >= result[i - 1]) {
                result[i - 1] = result[i] + 1;
            }
        }

        int sum = 0;
        for (int candyCount : result) {
            sum += candyCount;
        }

        return sum;
    }
};

// @lc code=end

