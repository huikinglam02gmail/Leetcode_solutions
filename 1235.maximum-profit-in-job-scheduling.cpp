/*
 * @lc app=leetcode id=1235 lang=cpp
 *
 * [1235] Maximum Profit in Job Scheduling
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <iostream>

class Solution {
public:
    int jobScheduling(std::vector<int>& startTime, std::vector<int>& endTime, std::vector<int>& profit) {
        std::vector<std::vector<int>> jobs;

        for (int i = 0; i < startTime.size(); ++i) {
            jobs.push_back({startTime[i], endTime[i], profit[i]});
        }

        std::sort(jobs.begin(), jobs.end(), [](const auto& a, const auto& b) {
            return a[0] < b[0];
        });

        int n = jobs.size();
        std::vector<int> result(n, 0);

        for (int i = n - 1; i >= 0; --i) {
            int currentProfit = jobs[i][2];
            auto it = std::lower_bound(jobs.begin(), jobs.end(), jobs[i][1], [](const auto& a, int val) {
                return a[0] < val;
            });

            int index = it - jobs.begin();

            if (index < n) {
                currentProfit += result[index];
            }

            if (i < n - 1) {
                result[i] = result[i + 1];
            }

            result[i] = std::max(result[i], currentProfit);
        }

        return result[0];
    }
};

// @lc code=end

