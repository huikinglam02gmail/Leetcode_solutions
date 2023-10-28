/*
 * @lc app=leetcode id=1963 lang=cpp
 *
 * [1963] Minimum Number of Swaps to Make the String Balanced
 */

// @lc code=start
#include <string>
#include <algorithm>
using std::min;
using std::string;
class Solution {
public:
    /*
    If we have a long streak of "]" before "[", we can switch neutralize them by taking the leftmost "]" with unbalance and switching with the rightmost "[" with unbalance. For example, as in Example 2, the balance is [-1, -2, -3, -2, -1, 0]. So, first switch 0 with 5: "[]][][". The balance is [1, 0, -1, 0, 1, 0, -1]. As we might see, by balancing index 0, we also balance index 1.
    */
    int minSwaps(string s) {
        int balance = 0;
        int result = 0;

        for (char c : s) {
            if (c == '[') {
                balance++;
            } else {
                balance--;
            }

            result = min(result, balance);
        }

        return (1 - result) / 2;
    }
};

// @lc code=end

