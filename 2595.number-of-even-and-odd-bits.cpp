/*
 * @lc app=leetcode id=2595 lang=cpp
 *
 * [2595] Number of Even and Odd Bits
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /**
     * Just do as described
     */
    std::vector<int> evenOddBit(int n) {
        std::string nString = std::bitset<32>(n).to_string();
        std::reverse(nString.begin(), nString.end());

        std::vector<int> result = {0, 0};

        for (int i = 0; i < nString.length(); i++) {
            if (nString[i] == '1') {
                result[i % 2]++;
            }
        }

        return result;
    }
};

// @lc code=end

