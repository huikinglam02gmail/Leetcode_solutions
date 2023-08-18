/*
 * @lc app=leetcode id=1615 lang=cpp
 *
 * [1615] Maximal Network Rank
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <tuple>

class Solution {
public:
    int maximalNetworkRank(int n, std::vector<std::vector<int>>& roads) {
        std::vector<int> degrees(n, 0);
        std::vector<std::vector<bool>> connected(n, std::vector<bool>(n, false));
        for (const auto& road : roads) {
            degrees[road[0]]++;
            degrees[road[1]]++;
            connected[std::min(road[0], road[1])][std::max(road[0], road[1])] = true;
        }

        int result = 0;
        for (int node1 = 0; node1 < n - 1; node1++) {
            for (int node2 = node1 + 1; node2 < n; node2++) {
                if (connected[node1][node2]) {
                    result = std::max(result, degrees[node1] + degrees[node2] - 1);
                } else {
                    result = std::max(result, degrees[node1] + degrees[node2]);
                }
            }
        }

        return result;
    }
};
// @lc code=end

