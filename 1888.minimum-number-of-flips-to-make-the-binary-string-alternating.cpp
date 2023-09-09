/*
 * @lc app=leetcode id=1888 lang=cpp
 *
 * [1888] Minimum Number of Flips to Make the Binary String Alternating
 */

// @lc code=start
#include <string>
#include <algorithm>

class Solution {
public:
    int minFlips(std::string s) {
        int parity[2][2] = {{0}};
        int n = s.length();
        int result = n;

        for (int i = 0; i < n; i++) {
            parity[i % 2][s[i] - '0']++;
        }

        for (int i = 0; i < n; i++) {
            result = std::min(result, parity[1][0] + parity[0][1]);
            result = std::min(result, parity[0][0] + parity[1][1]);
            parity[0][s[i] - '0']--;
            int temp = parity[0][0];
            parity[0][0] = parity[1][0];
            parity[1][0] = temp;
            temp = parity[0][1];
            parity[0][1] = parity[1][1];
            parity[1][1] = temp;
            parity[(n - 1) % 2][s[i] - '0']++;
        }

        return result;
    }
};

// @lc code=end

