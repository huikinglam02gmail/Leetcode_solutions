/*
 * @lc app=leetcode id=1481 lang=cpp
 *
 * [1481] Least Number of Unique Integers after K Removals
 */

// @lc code=start
#include <unordered_map>
#include <vector>
#include <algorithm>

class Solution {
public:
    int findLeastNumOfUniqueInts(std::vector<int>& arr, int k) {
        std::unordered_map<int, int> occur;
        for (int num : arr) {
            occur[num]++;
        }
        
        std::vector<std::pair<int, int>> kvp(occur.begin(), occur.end());
        std::sort(kvp.begin(), kvp.end(), [](const auto& a, const auto& b) {
            return a.second < b.second;
        });
        
        int n = kvp.size();
        int i = 0;
        while (k > 0) {
            if (kvp[i].second <= k) {
                k -= kvp[i].second;
                i++;
            } else {
                k = 0;
            }
        }
        
        return n - i;
    }
};

// @lc code=end

