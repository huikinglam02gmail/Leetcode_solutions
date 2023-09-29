/*
 * @lc app=leetcode id=896 lang=csharp
 *
 * [896] Monotonic Array
 */

// @lc code=start
public class Solution {
    public bool IsMonotonic(int[] nums) {
        int direction = 0;
        for (int i = 0; i < nums.Length - 1; i++) {
            if (direction == 0) {
                if (nums[i + 1] > nums[i]) {
                    direction = 1;
                } else if (nums[i + 1] < nums[i]) {
                    direction = -1;
                }
            } else {
                if (nums[i + 1] > nums[i] && direction != 1) {
                    return false;
                } else if (nums[i + 1] < nums[i] && direction != -1) {
                    return false;
                }
            }
        }
        return true;
    }
}

// @lc code=end

