/*
 * @lc app=leetcode id=673 lang=cpp
 *
 * [673] Number of Longest Increasing Subsequence
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>

using std::lower_bound;
using std::upper_bound;
using std::vector;

class Solution {
public:
    int findNumberOfLIS(std::vector<int>& nums) {
        vector<int> ends_decks {};
        vector<vector<int>> decks{};
        vector<vector<int>> paths{};

        for (int num : nums) {
            int deck_idx = lower_bound(ends_decks.begin(), ends_decks.end(), num) - ends_decks.begin();
            int n_paths = 1;

            if (deck_idx > 0) {
                int l = upper_bound(decks[deck_idx - 1].begin(), decks[deck_idx - 1].end(), - num) - decks[deck_idx - 1].begin();
                n_paths = paths[deck_idx - 1].back() - paths[deck_idx - 1][l];
            }

            if (deck_idx == ends_decks.size()) {
                decks.push_back(vector<int> { - num });
                ends_decks.push_back(num);
                paths.push_back(vector<int> {0, n_paths});
            } else {
                decks[deck_idx].push_back(-num);
                ends_decks[deck_idx] = num;
                paths[deck_idx].push_back(n_paths + paths[deck_idx].back());
            }
        }

        return paths.back().back();
    }
};

// @lc code=end

