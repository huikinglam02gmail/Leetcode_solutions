/*
 * @lc app=leetcode id=452 lang=cpp
 *
 * [452] Minimum Number of Arrows to Burst Balloons
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int findMinArrowShots(std::vector<std::vector<int>>& points) {
        std::sort(points.begin(), points.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] != b[0] ? a[0] < b[0] : a[1] < b[1];
        });
        
        int result = 1;
        int end = points[0][1];
        
        for (int i = 1; i < points.size(); i++) {
            if (points[i][0] > end) {
                result++;
                end = points[i][1];
            }
            end = std::min(end, points[i][1]);
        }
        
        return result;
    }
};

// @lc code=end

