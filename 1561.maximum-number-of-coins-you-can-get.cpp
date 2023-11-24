/*
 * @lc app=leetcode id=1561 lang=cpp
 *
 * [1561] Maximum Number of Coins You Can Get
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
     * Sort piles
     * Then add up second last from the back up to n // 3    
     */
    int maxCoins(std::vector<int>& piles) {
        int n = piles.size();
        std::sort(piles.begin(), piles.end());
        int result = 0;
        for (int i = n - 2; i >= n / 3; i -= 2) {
            result += piles[i];
        }
        return result;
    }
};
// @lc code=end

