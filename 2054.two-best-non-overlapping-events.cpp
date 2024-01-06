/*
 * @lc app=leetcode id=2054 lang=cpp
 *
 * [2054] Two Best Non-Overlapping Events
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    int maxTwoEvents(std::vector<std::vector<int>>& events) {
        std::sort(events.begin(), events.end(), [](const auto& a, const auto& b) {
            return a[1] < b[1];
        });

        std::priority_queue<std::vector<int>> heap;
        int result = 0;

        for (const auto& ev : events) {
            heap.push({ev[2], -ev[0]});
        }

        for (const auto& ev : events) {
            while (!heap.empty() && -heap.top()[1] <= ev[1]) {
                heap.pop();
            }

            int current = 0;
            if (!heap.empty()) {
                current += heap.top()[0];
            }

            result = std::max(result, ev[2] + current);
        }

        return result;
    }
};

// @lc code=end

