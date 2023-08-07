/*
 * @lc app=leetcode id=1840 lang=cpp
 *
 * [1840] Maximum Building Height
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int maxBuilding(int n, std::vector<std::vector<int>>& restrictions) {
        std::vector<std::vector<int>> restrictionsList = restrictions;
        restrictionsList.push_back({1, 0});
        std::sort(restrictionsList.begin(), restrictionsList.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] < b[0];
        });

        if (restrictionsList.back()[0] != n) {
            restrictionsList.push_back({n, n - 1});
        }

        int resultLeftToRight = Scan(restrictionsList);
        std::reverse(restrictionsList.begin(), restrictionsList.end());
        int resultRightToLeft = Scan(restrictionsList);

        return std::min(resultLeftToRight, resultRightToLeft);
    }

private:
    int Scan(std::vector<std::vector<int>>& restrictions) {
        int n = restrictions.size();
        int result = 0;

        for (int i = 0; i < n - 1; i++) {
            int h = restrictions[i][1] + std::abs(restrictions[i + 1][0] - restrictions[i][0]);

            if (h > restrictions[i + 1][1]) {
                h = restrictions[i + 1][1] + (h - restrictions[i + 1][1]) / 2;
            }

            result = std::max(result, h);
            restrictions[i + 1][1] = std::min(restrictions[i + 1][1], h);
        }

        return result;
    }
};

// @lc code=end

