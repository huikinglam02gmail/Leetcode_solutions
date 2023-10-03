/*
 * @lc app=leetcode id=1512 lang=cpp
 *
 * [1512] Number of Good Pairs
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    int numIdenticalPairs(std::vector<int>& nums) {
        std::unordered_map<int, int> hashTable;

        for (int num : nums) {
            if (hashTable.find(num) != hashTable.end()) {
                hashTable[num]++;
            } else {
                hashTable[num] = 1;
            }
        }

        int result = 0;

        for (const auto& kvp : hashTable) {
            int count = kvp.second;
            result += count * (count - 1) / 2;
        }

        return result;
    }
};
// @lc code=end

