/*
 * @lc app=leetcode id=1739 lang=csharp
 *
 * [1739] Building Boxes
 */

// @lc code=start
public class Solution {
    public int MinimumBoxes(int n) {
        int cur = 0;
        int nxt = 1;
        int lastSize = 1;
        
        while (n > cur + nxt) {
            cur += nxt;
            lastSize += 1;
            nxt += lastSize;
        }
        
        int remainder = 0;
        
        while (cur + remainder < n) {
            cur += remainder;
            remainder += 1;
        }
        
        return nxt + remainder - lastSize;
    }
}

// @lc code=end

