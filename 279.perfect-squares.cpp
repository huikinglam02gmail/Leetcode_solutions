/*
 * @lc app=leetcode id=279 lang=cpp
 *
 * [279] Perfect Squares
 */

// @lc code=start
#include <vector>
#include <cmath>

class Solution {
public:
    int numSquares(int n) {
        std::vector<int> perfect;
        for (int i = 1; i <= 100; ++i) {
            perfect.push_back(i * i);
            if (i * i == n) {
                return 1;
            }
        }

        int index = 0;
        while (n > perfect[index]) {
            if (std::find(perfect.begin(), perfect.end(), n - perfect[index]) != perfect.end()) {
                return 2;
            }
            ++index;
        }

        while (n % 4 == 0) {
            n /= 4;
        }

        if (n % 8 == 7) {
            return 4;
        } else {
            return 3;
        }
    }
};

// @lc code=end

