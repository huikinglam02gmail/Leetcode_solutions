/*
 * @lc app=leetcode id=338 lang=cpp
 *
 * [338] Counting Bits
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        int cur = -1;
        vector<int> result = { 0 };
        
        for (int i = 1; i <= n; i++) {
            while (i >= (1 << (cur + 1))) {
                cur++;
            }
            result.push_back(result[i - (1 << cur)] + 1);
        }
        
        return result;
    }
};
// @lc code=end

