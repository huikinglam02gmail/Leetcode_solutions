/*
 * @lc app=leetcode id=2483 lang=cpp
 *
 * [2483] Minimum Penalty for a Shop
 */

// @lc code=start
#include <string>

class Solution {
public:
    int bestClosingTime(std::string customers) {
        int n = customers.size();
        int result = n;
        int minimum = -count(customers.begin(), customers.end(), 'N');
        int current = minimum;
        
        for (int i = n - 1; i >= 0; i--) {
            if (customers[i] == 'N') {
                current -= 1;
            }
            else {
                current += 1;
            }
            if (current <= minimum) {
                minimum = current;
                result = i;
            }
        }
        
        return result;
    }
};
// @lc code=end

