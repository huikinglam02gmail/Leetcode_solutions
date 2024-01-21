/*
 * @lc app=leetcode id=2566 lang=cpp
 *
 * [2566] Maximum Difference by Remapping a Digit
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /**
     * There are only 10 digits. In terms of a map, there are 100 keys.
     * Use the 100 keys and record max and min of the result and take the difference.
     */
    int minMaxDifference(int num) {
        std::vector<int> master;
        int temp = num;
        while (temp > 0) {
            master.insert(master.begin(), temp % 10);
            temp /= 10;
        }

        long long minResult = LLONG_MAX;
        long long maxResult = LLONG_MIN;

        for (int i = 0; i < 10; i++) {
            if (std::find(master.begin(), master.end(), i) != master.end()) {
                for (int j = 0; j < 10; j++) {
                    long long modified = 0;

                    for (int k = 0; k < master.size(); k++) {
                        if (master[k] == i)
                            modified += j;
                        else
                            modified += master[k];

                        modified *= 10;
                    }

                    minResult = std::min(minResult, modified / 10);
                    maxResult = std::max(maxResult, modified / 10);
                }
            }
        }

        return static_cast<int>(maxResult - minResult);
    }
};

// @lc code=end

