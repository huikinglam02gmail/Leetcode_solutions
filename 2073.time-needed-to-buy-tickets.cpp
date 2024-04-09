/*
 * @lc app=leetcode id=2073 lang=cpp
 *
 * [2073] Time Needed to Buy Tickets
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int timeRequiredToBuy(std::vector<int>& tickets, int k) {
        int result = 0;
        while (tickets[k] > 0) {
            for (int i = 0; i < tickets.size(); i++) {
                if (tickets[i] > 0) {
                    result++;
                    tickets[i]--;
                }
                if (i == k && tickets[i] == 0) {
                    return result;
                }
            }
        }
        return -1;
    }
};

// @lc code=end

