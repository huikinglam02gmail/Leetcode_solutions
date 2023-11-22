/*
 * @lc app=leetcode id=1424 lang=cpp
 *
 * [1424] Diagonal Traverse II
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    std::vector<int> findDiagonalOrder(std::vector<std::vector<int>>& nums) {
        std::vector<int> result;
        int m = nums.size();
        std::unordered_map<int, std::vector<std::pair<int, int>>> hashTable;

        for (int i = 0; i < m; i++) {
            int l = nums[i].size();
            for (int j = 0; j < l; j++) {
                int key = i + j;
                hashTable[key].push_back({i, j});
            }
        }

        std::vector<int> keys;
        for (const auto& entry : hashTable) {
            keys.push_back(entry.first);
        }

        std::sort(keys.begin(), keys.end());

        for (int key : keys) {
            std::sort(hashTable[key].begin(), hashTable[key].end(), [](const auto& a, const auto& b) {
                return a.first > b.first;
            });

            for (const auto& pair : hashTable[key]) {
                result.push_back(nums[pair.first][pair.second]);
            }
        }

        return result;
    }
};

// @lc code=end

