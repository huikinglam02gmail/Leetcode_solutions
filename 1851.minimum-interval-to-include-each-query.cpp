/*
 * @lc app=leetcode id=1851 lang=cpp
 *
 * [1851] Minimum Interval to Include Each Query
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<int> minInterval(std::vector<std::vector<int>>& intervals, std::vector<int>& queries) {
        std::vector<std::pair<int, int>> queriesWithIndex;
        for (int i = 0; i < queries.size(); i++) {
            queriesWithIndex.push_back(std::make_pair(queries[i], i));
        }
        std::sort(queriesWithIndex.begin(), queriesWithIndex.end());

        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a[0] != b[0]) {
                return a[0] < b[0];
            }
            return a[1] < b[1];
        });

        std::priority_queue<std::pair<int, int>> heap;
        std::vector<int> result(queries.size(), -1);
        int j = 0;
        for (int i = 0; i < queriesWithIndex.size(); i++) {
            int q = queriesWithIndex[i].first;
            int ind = queriesWithIndex[i].second;
            
            while (j < intervals.size() && intervals[j][0] <= q) {
                heap.push(std::make_pair(- intervals[j][1] + intervals[j][0] - 1, intervals[j][1]));
                j++;
            }
            
            while (!heap.empty() && heap.top().second < q) {
                heap.pop();
            }

            if (!heap.empty()) {
                result[ind] = - heap.top().first;
            }
        }       
        return result;
    }
};
// @lc code=end

