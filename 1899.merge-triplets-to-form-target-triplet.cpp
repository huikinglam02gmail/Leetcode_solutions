/*
 * @lc app=leetcode id=1899 lang=cpp
 *
 * [1899] Merge Triplets to Form Target Triplet
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    bool mergeTriplets(std::vector<std::vector<int>>& triplets, std::vector<int>& target) {
        std::vector<int> satisfy(3);

        for (int i = 0; i < triplets.size(); i++) {
            if (triplets[i][0] <= target[0] && triplets[i][1] <= target[1] && triplets[i][2] <= target[2]) {
                satisfy[0] = std::max(satisfy[0], triplets[i][0]);
                satisfy[1] = std::max(satisfy[1], triplets[i][1]);
                satisfy[2] = std::max(satisfy[2], triplets[i][2]);
            }
        }

        return satisfy[0] == target[0] && satisfy[1] == target[1] && satisfy[2] == target[2];
    }
};

// @lc code=end

