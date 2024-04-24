/*
 * @lc app=leetcode id=1137 lang=cpp
 *
 * [1137] N-th Tribonacci Number
 */

// @lc code=start
class Solution {
public:
    int tribonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1 || n == 2) {
            return 1;
        } else {
            int t0 = 0, t1 = 1, t2 = 1;
            int t3 = t0 + t1 + t2;
            for (int i = 3; i < n; i++) {
                int temp = t3;
                t3 = t3 + t2 + t1;
                t0 = t1;
                t1 = t2;
                t2 = temp;
            }
            return t3;
        }
    }
};

// @lc code=end

