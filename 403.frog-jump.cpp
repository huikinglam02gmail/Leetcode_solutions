/*
 * @lc app=leetcode id=403 lang=cpp
 *
 * [403] Frog Jump
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    bool canCross(std::vector<int>& stones) {
        std::unordered_map<int, int> stoneTable;
        for (int i = 0; i < stones.size(); i++) {
            stoneTable[stones[i]] = i;
        }

        std::vector<std::unordered_set<int>> kSet(stones.size());
        kSet[0].insert(0);

        for (int i = 0; i < stones.size(); i++) {
            for (int item : kSet[i]) {
                for (int j = -1; j <= 1; j++) {
                    if (item + j >= 1 && stoneTable.count(stones[i] + item + j)) {
                        kSet[stoneTable[stones[i] + item + j]].insert(item + j);
                    }
                }
            }
        }

        return !kSet[stones.size() - 1].empty();
    }
};

// @lc code=end

