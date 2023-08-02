/*
 * @lc app=leetcode id=46 lang=cpp
 *
 * [46] Permutations
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<std::vector<int>> permute(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::vector<int> currentList;
        std::unordered_set<int> usedIndexes;
        permuteHelper(nums, currentList, usedIndexes, result);
        return result;
    }

private:
    void permuteHelper(const std::vector<int>& nums, std::vector<int>& currentList, std::unordered_set<int>& usedIndexes, std::vector<std::vector<int>>& result) {
        if (currentList.size() == nums.size()) {
            result.push_back(currentList);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (usedIndexes.find(i) == usedIndexes.end()) {
                currentList.push_back(nums[i]);
                usedIndexes.insert(i);
                permuteHelper(nums, currentList, usedIndexes, result);
                usedIndexes.erase(i);
                currentList.pop_back();
            }
        }
    }
};

// @lc code=end

