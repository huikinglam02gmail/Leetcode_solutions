/*
 * @lc app=leetcode id=1727 lang=cpp
 *
 * [1727] Largest Submatrix With Rearrangements
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int largestRectangleArea(std::vector<int>& heights) {
        int n = heights.size();
        std::vector<int> h = {0};
        h.insert(h.end(), heights.begin(), heights.end());
        h.push_back(0);
        
        std::vector<std::pair<int, int>> stack;
        int maxArea = 0;
        
        for (int i = 0; i < h.size(); ++i) {
            int index = i;
            while (!stack.empty() && stack.back().second > h[i]) {
                auto [ind, height] = stack.back();
                stack.pop_back();
                int area = height * (i - ind);
                maxArea = std::max(maxArea, area);
            }
            stack.emplace_back(index, h[i]);
        }
        
        return maxArea;
    }
    
    int largestSubmatrix(std::vector<std::vector<int>>& matrix) {
        int maxArea = 0;
        int m = matrix.size();
        int n = matrix[0].size();
        
        std::vector<int> row(n, 0);
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                row[j] = matrix[i][j] ? row[j] + 1 : 0;
            }
            
            std::vector<int> sortedRow(row);
            std::sort(sortedRow.begin(), sortedRow.end());
            
            maxArea = std::max(maxArea, largestRectangleArea(sortedRow));
        }
        
        return maxArea;
    }
};

// @lc code=end

