/*
 * @lc app=leetcode id=1819 lang=cpp
 *
 * [1819] Number of Different Subsequences GCDs
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <numeric> // for std::gcd
using std::gcd;
using std::max_element;
using std::unordered_set;

class Solution
{
public:
    int countDifferentSubsequenceGCDs(std::vector<int>& nums) {
        unordered_set<int> numsSet(nums.begin(), nums.end());
        int T = *max_element(nums.begin(), nums.end()) + 1;
        int res = 0;
        for (int x = 1; x < T; x++) {
            int g = 0;
            for (int y = x; y < T; y += x) {
                if (numsSet.find(y) != numsSet.end()) {
                    g = gcd(g, y);
                }
                if (g == x) {
                    res++;
                    break;
                }
            }
        }
        return res;
    }
};
// @lc code=end

