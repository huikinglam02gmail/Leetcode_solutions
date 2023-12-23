/*
 * @lc app=leetcode id=1496 lang=cpp
 *
 * [1496] Path Crossing
 */

// @lc code=start
#include <set>

class Solution {
public:
    bool isPathCrossing(std::string path) {
        std::set<std::pair<int, int>> seen;
        seen.insert({0, 0});
        int x = 0, y = 0;

        for (char c : path) {
            if (c == 'N') {
                y += 1;
            } else if (c == 'E') {
                x += 1;
            } else if (c == 'S') {
                y -= 1;
            } else {
                x -= 1;
            }

            if (seen.find({x, y}) != seen.end()) {
                return true;
            } else {
                seen.insert({x, y});
            }
        }

        return false;
    }
};

// @lc code=end

