/*
 * @lc app=leetcode id=2485 lang=cpp
 *
 * [2485] Find the Pivot Integer
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int pivotInteger(int n) {
        std::vector<int> prefix(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + i;
        }
        for (int x = 1; x <= n; x++) {
            if (prefix[x] - prefix[0] == prefix[n] - prefix[x - 1]) {
                return x;
            }
        }
        return -1;
    }
};

// @lc code=end

