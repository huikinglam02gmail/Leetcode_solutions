/*
 * @lc app=leetcode id=661 lang=cpp
 *
 * [661] Image Smoother
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int m = img.size();
        int n = img[0].size();
        vector<vector<int>> result(m, vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int avg = 0;
                int counter = 0;

                for (int k = -1; k <= 1; k++) {
                    for (int l = -1; l <= 1; l++) {
                        if (0 <= i + k && i + k < m && 0 <= j + l && j + l < n) {
                            avg += img[i + k][j + l];
                            counter++;
                        }
                    }
                }

                result[i][j] = avg / counter;
            }
        }

        return result;
    }
};

// @lc code=end

