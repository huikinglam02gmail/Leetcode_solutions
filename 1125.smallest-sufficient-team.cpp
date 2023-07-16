/*
 * @lc app=leetcode id=1125 lang=cpp
 *
 * [1125] Smallest Sufficient Team
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>

using std::pair;
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    std::vector<int> smallestSufficientTeam(vector<string>& reqSkills, vector<vector<string>>& people) {
        unordered_map<string, int> skillSet {};
        int ns = reqSkills.size();

        for (int i = 0; i < ns; i++) {
            skillSet[reqSkills[i]] = i;
        }

        unordered_map<int, vector<int>> dp {};
        dp.reserve(1 << ns);
        dp.insert({0, vector<int>{}});

        for (int i = 0; i < people.size(); i++) {
            int peopleMask = 0;

            for (const auto& skill : people[i]) {
                peopleMask ^= (1 << skillSet[skill]);
            }

            for (auto it = dp.begin(); it != dp.end(); it++)
            {
                int skillMask = it -> first;
                vector<int> team = it -> second;
                int newMask = (skillMask | peopleMask);

                if (dp.find(newMask) == dp.end() || dp[newMask].size() > 1 + team.size()) {
                    dp[newMask] = vector<int>(team);
                    dp[newMask].push_back(i);
                }
            }
        }

        return dp[(1 << ns) - 1];
    }
};

// @lc code=end

