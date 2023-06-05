/*
 * @lc app=leetcode id=1739 lang=cpp
 *
 * [1739] Building Boxes
 */

// @lc code=start
class Solution {
public:
    int minimumBoxes(int n) {
        int cur {0};
        int nxt {1};
        int lastSize {1};
        
        while (n > cur + nxt) {
            cur += nxt;
            lastSize++;
            nxt += lastSize;
        }
        
        int remainder = 0;
        
        while (cur + remainder < n) {
            cur += remainder;
            remainder++;
        }
        
        return nxt + remainder - lastSize;
    }
};
// @lc code=end

