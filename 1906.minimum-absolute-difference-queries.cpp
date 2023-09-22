/*
 * @lc app=leetcode id=1906 lang=cpp
 *
 * [1906] Minimum Absolute Difference Queries
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <limits>

class Solution {
public:
    /*
     * 1 <= nums[i] <= 100
     * We can save indices of appearance of each nums
     * Then binary search for each query
     */
    std::vector<int> minDifference(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        std::unordered_map<int, std::vector<int>> hashTable;
        for (int i = 0; i < nums.size(); i++) {
            hashTable[nums[i]].push_back(i);
        }
        
        std::vector<int> allNums;
        for (const auto& entry : hashTable) {
            allNums.push_back(entry.first);
        }
        std::sort(allNums.begin(), allNums.end());
        
        std::vector<int> result;
        
        for (const auto& query : queries) {
            int l = query[0];
            int r = query[1];
            std::vector<int> appeared;
            result.push_back(std::numeric_limits<int>::max());
            
            for (int allNum : allNums) {
                auto leftIter = std::lower_bound(hashTable[allNum].begin(), hashTable[allNum].end(), l);
                auto rightIter = std::upper_bound(hashTable[allNum].begin(), hashTable[allNum].end(), r);
                
                if (rightIter - leftIter > 0) {
                    appeared.push_back(allNum);
                    if (appeared.size() > 1) {
                        result.back() = std::min(result.back(), appeared.back() - appeared[appeared.size() - 2]);
                    }
                }
            }
            
            if (result.back() == std::numeric_limits<int>::max()) {
                result.back() = -1;
            }
        }
        
        return result;
    }
};

// @lc code=end

