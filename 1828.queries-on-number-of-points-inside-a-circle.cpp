/*
 * @lc app=leetcode id=1828 lang=cpp
 *
 * [1828] Queries on Number of Points Inside a Circle
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> result;
        for (const auto& query : queries) {
            int x = query[0];
            int y = query[1];
            int r = query[2];
            int count = 0;
            for (const auto& point : points) {
                int x1 = point[0];
                int y1 = point[1];
                if ((x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r) {
                    count++;
                }
            }
            result.push_back(count);
        }
        return result;
    }
};

// @lc code=end

