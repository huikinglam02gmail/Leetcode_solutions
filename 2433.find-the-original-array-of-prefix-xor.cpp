/*
 * @lc app=leetcode id=2433 lang=cpp
 *
 * [2433] Find The Original Array of Prefix Xor
 */

// @lc code=start
#include <vector>

class Solution {
public:
    std::vector<int> findArray(std::vector<int>& pref) {
        int n = pref.size();
        for (int i = n - 1; i > 0; i--) {
            pref[i] ^= pref[i - 1];
        }
        return pref;
    }
};

// @lc code=end

