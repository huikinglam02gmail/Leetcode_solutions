/*
 * @lc app=leetcode id=1894 lang=cpp
 *
 * [1894] Find the Student that Will Replace the Chalk
 */

// @lc code=start
#include <algorithm>
using std::upper_bound;
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        vector<long long> prefix;
        prefix.push_back(0);

        for (int num : chalk) {
            prefix.push_back(prefix.back() + num);
        }

        long long remainder = static_cast<long long>(k) % prefix.back();

        return upper_bound(prefix.begin(), prefix.end(), remainder) - prefix.begin() - 1;
    }
};
// @lc code=end

