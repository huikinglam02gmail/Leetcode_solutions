/*
 * @lc app=leetcode id=2064 lang=cpp
 *
 * [2064] Minimized Maximum of Products Distributed to Any Store
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int ceilDiv(int a, int b) {
        return (a + b - 1) / b;
    }

    int minimizedMaximum(int n, std::vector<int>& quantities) {
        int l = 1, r = *std::max_element(quantities.begin(), quantities.end());
        while (l < r) {
            int mid = l + (r - l) / 2;
            int numPeople = 0;
            for (int q : quantities) {
                numPeople += ceilDiv(q, mid);
            }
            if (numPeople <= n) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};

// @lc code=end

