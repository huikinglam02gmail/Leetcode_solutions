/*
 * @lc app=leetcode id=2870 lang=cpp
 *
 * [2870] Minimum Number of Operations to Make Array Empty
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    /*
    All counts must be 2 * m + 3 * n
    The best strategy is to take:
    1. count // 3 rounds of the 2nd operation, and if (count - 3 * (count / 3)) % 2 == 0, add (count - 3 * (count / 3)) / 2 of the 1st operation
    2. Take (count / 3 - 1) rounds of the 2nd operation, and if (count - 3 * (count / 3 - 1)) % 2 == 0, add (count - 3 * (count / 3 - 1)) / 2 of the 1st operation
    return -1 otherwise
    */
    int minOperations(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }

        int result = 0;
        for (const auto& entry : counts) {
            int v = entry.second;
            if ((v - 3 * (v / 3)) % 2 == 0) {
                result += v / 3 + (v - 3 * (v / 3)) / 2;
            } else if (v / 3 > 0 && (v - 3 * ((v / 3) - 1)) % 2 == 0) {
                result += v / 3 - 1 + (v - 3 * ((v / 3) - 1)) / 2;
            } else {
                return -1;
            }
        }
        return result;
    }
};


// @lc code=end

