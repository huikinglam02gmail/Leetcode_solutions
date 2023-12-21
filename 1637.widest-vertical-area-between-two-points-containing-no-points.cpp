/*
 * @lc app=leetcode id=1637 lang=cpp
 *
 * [1637] Widest Vertical Area Between Two Points Containing No Points
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        unordered_set<int> xPos;
        
        for (const auto& point : points) {
            xPos.insert(point[0]);
        }

        vector<int> xList(xPos.begin(), xPos.end());
        sort(xList.begin(), xList.end());

        int result = 0;
        for (int i = 0; i < xList.size() - 1; ++i) {
            result = max(result, xList[i + 1] - xList[i]);
        }

        return result;
    }
};

// @lc code=end

