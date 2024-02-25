/*
 * @lc app=leetcode id=2937 lang=cpp
 *
 * [2937] Make Three Strings Equal
 */

// @lc code=start
#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int findMinimumOperations(std::string s1, std::string s2, std::string s3) {
        std::vector<std::string> lengthOrder = {s1, s2, s3};
        std::sort(lengthOrder.begin(), lengthOrder.end(), [](const std::string& a, const std::string& b) {
            return a.size() < b.size();
        });
        int i = lengthOrder[0].size();
        while (i > 0 && (lengthOrder[1].substr(0, i) != lengthOrder[0].substr(0, i) || lengthOrder[2].substr(0, i) != lengthOrder[0].substr(0, i))) {
            i--;
        }
        if (i == 0) {
            return -1;
        } else {
            int sum = 0;
            for (const auto& s : lengthOrder) {
                sum += s.size() - i;
            }
            return sum;
        }
    }
};

// @lc code=end

