/*
 * @lc app=leetcode id=1356 lang=cpp
 *
 * [1356] Sort Integers by The Number of 1 Bits
 */

// @lc code=start
#include <vector>
#include <algorithm>

using std::sort;

class Solution {
public:
    static bool compare(int a, int b) {
        int count_a = __builtin_popcount(a);  // Count the number of set bits in a
        int count_b = __builtin_popcount(b);  // Count the number of set bits in b
        return count_a == count_b ? a < b : count_a < count_b;
    }

    std::vector<int> sortByBits(std::vector<int>& arr) 
    {
        sort(arr.begin(), arr.end());
        std::sort(arr.begin(), arr.end(), compare);
        return arr;
    }
};

// @lc code=end

