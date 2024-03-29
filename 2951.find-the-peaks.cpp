/*
 * @lc app=leetcode id=2951 lang=cpp
 *
 * [2951] Find the Peaks
 */

// @lc code=start
#include <vector>

class Solution {
public:
    std::vector<int> findPeaks(std::vector<int>& mountain) {
        std::vector<int> result;
        int n = mountain.size();
        for (int i = 1; i < n - 1; i++) {
            if (mountain[i - 1] < mountain[i] && mountain[i] > mountain[i + 1]) {
                result.push_back(i);
            }
        }
        return result;
    }
};

// @lc code=end

