/*
 * @lc app=leetcode id=335 lang=cpp
 *
 * [335] Self Crossing
 */

// @lc code=start
#include <vector>

class Solution {
public:
    /*
     * Two points to note: 
     * 1. The Cartesian coordinate system is symmetric with 90-degree rotations
     * 2. To cross a previous path with a future step, one can cross from left, right, or from below
     */
    bool isSelfCrossing(std::vector<int>& distance) {
        int b = 0, c = 0, d = 0, e = 0, f = 0;
        for (int a : distance) {
            // cross from left
            if (d > 0 && d >= b && a >= c)
                return true;
            // cross from below
            if (e > 0 && c <= a + e && b == d)
                return true;
            // cross from the right
            if (f > 0 && b <= d && d <= b + f && e <= c && c <= a + e)
                return true;
            f = e;
            e = d;
            d = c;
            c = b;
            b = a;
        }
        return false;
    }
};

// @lc code=end

