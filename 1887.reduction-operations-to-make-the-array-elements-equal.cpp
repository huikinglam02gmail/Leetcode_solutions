/*
 * @lc app=leetcode id=1887 lang=cpp
 *
 * [1887] Reduction Operations to Make the Array Elements Equal
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int reductionOperations(std::vector<int>& nums) {
        std::unordered_map<int, int> hashTable;
        for (int num : nums) {
            hashTable[num]++;
        }

        std::vector<int> keys;
        for (const auto& pair : hashTable) {
            keys.push_back(pair.first);
        }
        std::sort(keys.begin(), keys.end());

        int result = 0;
        int current = 0;
        int n = keys.size();

        for (int i = n - 1; i > 0; i--) {
            current += hashTable[keys[i]];
            result += current;
        }

        return result;
    }
};

// @lc code=end

