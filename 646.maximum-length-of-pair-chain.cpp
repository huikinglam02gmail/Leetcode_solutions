/*
 * @lc app=leetcode id=646 lang=cpp
 *
 * [646] Maximum Length of Pair Chain
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int findLongestChain(std::vector<std::vector<int>>& pairs) {
        std::sort(pairs.begin(), pairs.end(), [](const std::vector<int>& x, const std::vector<int>& y) {
            return x[1] < y[1];
        });
        
        std::vector<int> chain;
        
        for (const auto& pair : pairs) {
            if (chain.empty() || pair[0] > chain.back()) {
                chain.push_back(pair[1]);
            }
        }
        
        return chain.size();
    }
};

// @lc code=end

