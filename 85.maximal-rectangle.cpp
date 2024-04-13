/*
 * @lc app=leetcode id=85 lang=cpp
 *
 * [85] Maximal Rectangle
 */

// @lc code=start
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector<int> array = {0};
        for (int i : heights) array.push_back(i);
        array.push_back(0);
        stack<pair<int, int>> st;
        int max_area = 0;
        for (int i = 0; i < array.size(); ++i) {
            int index = i;
            while (!st.empty() && array[i] < st.top().second) {
                index = st.top().first;
                int height = st.top().second;
                st.pop();
                int area = height * (i - index);
                max_area = max(max_area, area);
            }
            st.push({index, array[i]});
        }
        return max_area;
    }
    
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if (m == 0) return 0;
        int n = matrix[0].size();
        vector<vector<int>> numbers(m, vector<int>(n, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                numbers[i][j] = matrix[i][j] - '0';
            }
        }
        int max_area = 0;
        vector<int> row(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                row[j] = (numbers[i][j] == 0) ? 0 : row[j] + numbers[i][j];
            }
            max_area = max(max_area, largestRectangleArea(row));
        }
        return max_area;
    }
};

// @lc code=end

