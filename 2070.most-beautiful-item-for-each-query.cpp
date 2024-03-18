/*
 * @lc app=leetcode id=2070 lang=cpp
 *
 * [2070] Most Beautiful Item for Each Query
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> maximumBeauty(std::vector<std::vector<int>>& items, std::vector<int>& queries) {
        std::vector<std::pair<int, int>> Q;
        for (int i = 0; i < queries.size(); ++i) {
            Q.push_back({queries[i], i});
        }
        std::sort(Q.begin(), Q.end());
        std::sort(items.begin(), items.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });
        
        std::vector<int> result(queries.size(), 0);
        int iQ = 0, iItem = 0;
        int maxSoFar = 0;
        for (int i = 0; i < Q.size(); ++i) {
            while (iItem < items.size() && items[iItem][0] <= Q[i].first) {
                maxSoFar = std::max(maxSoFar, items[iItem][1]);
                ++iItem;
            }
            result[Q[i].second] = maxSoFar;
        }
        return result;
    }
};

// @lc code=end

