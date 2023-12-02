/*
 * @lc app=leetcode id=2001 lang=cpp
 *
 * [2001] Number of Pairs of Interchangeable Rectangles
 */

// @lc code=start
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long interchangeableRectangles(std::vector<std::vector<int>>& rectangles) {
        std::unordered_map<double, long long> hashTable;
        long long result = 0;

        for (const auto& rectangle : rectangles) {
            double ratio = static_cast<double>(rectangle[1]) / rectangle[0];
            hashTable[ratio] = 1 + hashTable[ratio];
        }

        for (const auto& entry : hashTable) {
            long long count = entry.second;
            result += count * (count - 1) / 2;
        }

        return result;
    }
};

// @lc code=end

