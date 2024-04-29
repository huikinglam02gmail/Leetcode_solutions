/*
 * @lc app=leetcode id=2997 lang=cpp
 *
 * [2997] Minimum Number of Operations to Make Array XOR Equal to K
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

class Solution {
public:
    /*
    break down k into binary representation
    for each num, add # of 0 and 1 bits in each slot.
    */
    int minOperations(std::vector<int>& nums, int k) {
        int bitsToUse = static_cast<int>(std::bitset<32>(k).to_string().length());
        for (int num : nums) {
            bitsToUse = std::max(bitsToUse, static_cast<int>(std::bitset<32>(num).to_string().length()));
        }
        std::vector<int> counts(bitsToUse, 0);
        for (int num : nums) {
            for (int i = 0; i < bitsToUse; i++) {
                if ((num & (1 << i)) != 0) {
                    counts[i]++;
                }
            }
        }
        int result = 0;
        int n = nums.size();
        for (int i = 0; i < bitsToUse; i++) {
            if (((k & (1 << i)) == 0) ^ (counts[i] % 2 == 0)) {
                result++;
            }
        }
        return result;
    }
};

// @lc code=end

