/*
 * @lc app=leetcode id=1239 lang=cpp
 *
 * [1239] Maximum Length of a Concatenated String with Unique Characters
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    /**
     * This is a DP problem
     * 1 <= arr.size() <= 16, small enough to do it semi-brute force
     * We can find all possible combinations inside arr which do not have overlapping characters
     * We use the dp vector to keep all the possible used characters
     * dp[i] = all possible sets of unique characters if we use arr[0:i+1]
     */
    int maxLength(std::vector<std::string>& arr) {
        vector<bitset<26>> dp = {bitset<26>()};
        int res = 0;
        for (auto& s : arr) {
            bitset<26> a;
            for (char c : s)
                a.set(c - 'a');
            int n = a.count();
            if (n < s.size()) continue;

            for (int i = dp.size() - 1; i >= 0; --i) {
                bitset c = dp[i];
                if ((c & a).any()) continue;
                dp.push_back(c | a);
                res = max(res, (int)c.count() + n);
            }
        }
        return res;
    }
};

// @lc code=end

