/*
 * @lc app=leetcode id=2044 lang=cpp
 *
 * [2044] Count Number of Maximum Bitwise-OR Subsets
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    int countMaxOrSubsets(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> subSetMask(1 << n, 0);
        int i = 0;
        std::unordered_map<int, int> hashTable;

        for (int mask = 1; mask < (1 << n); mask++) {
            while (mask >= (1 << i)) {
                i++;
            }
            subSetMask[mask] = nums[i - 1] | subSetMask[mask - (1 << (i - 1))];
            hashTable[subSetMask[mask]] = hashTable[subSetMask[mask]] + 1;
        }

        return hashTable[getMaxKey(hashTable)];
    }

private:
    int getMaxKey(std::unordered_map<int, int>& hashTable) {
        int maxKey = INT_MIN;
        for (const auto& pair : hashTable) {
            maxKey = std::max(maxKey, pair.first);
        }
        return maxKey;
    }
};

// @lc code=end

