/*
 * @lc app=leetcode id=1611 lang=cpp
 *
 * [1611] Minimum One Bit Operations to Make Integers Zero
 */

// @lc code=start
class Solution {
public:
    int minimumOneBitOperations(int n) {
        if (n == 0) return 0;
        int l = 32 - __builtin_clz(n); // Number of bits needed to represent n
        return (1 << l) - 1 - minimumOneBitOperations(n - (1 << (l - 1)));
    }
};

// @lc code=end

